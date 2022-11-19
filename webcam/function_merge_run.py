"""
import sys

sys.path.append('../')
"""
from GazeTracking.gaze_tracking import GazeTracking
from Headpose_Detection import headpose
from Headpose_Detection.utils import Color

from cvlib.object_detection import draw_bbox

import argparse
import cvlib
import cv2

def pre_headpose_detection(args: dict):
    filename = args["input_file"]
    out = ''

    if filename is None:
        isVideo = False
        cap = cv2.VideoCapture(0)
        cap.set(3, args['wh'][0])
        cap.set(4, args['wh'][1])
    else:
        isVideo = True
        cap = cv2.VideoCapture(filename)
        fps = cap.get(cv2.CAP_PROP_FPS)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(args["output_file"], fourcc, fps, (width, height))

    # Initialize head pose detection
    hpd = headpose.HeadposeDetection(args["landmark_type"], args["landmark_predictor"])

    return cap, isVideo, hpd, out

def merge_detection(gaze, webcam, args: dict):
    cap, isVideo, hpd, out = pre_headpose_detection(args)

    while(cap.isOpened()):
        # We get a new frame from the webcam
        # _, frame = webcam.read()
        ret, frame = cap.read()

        # We send this frame to GazeTracking to analyze it
        gaze.refresh(frame)

        frame = gaze.annotated_frame()
        text = ""

        ## gaze tracking start
        if gaze.is_blinking():  # 깜빡임
            text = "Blinking"
        elif gaze.is_right():
            text = "Looking right"
        elif gaze.is_left():
            text = "Looking left"
        elif gaze.is_center():
            text = "Looking center"

        cv2.putText(frame, text, (5, 28), cv2.FONT_HERSHEY_DUPLEX, 1, Color.red, 2)

        left_pupil = gaze.pupil_left_coords()
        right_pupil = gaze.pupil_right_coords()
        cv2.putText(frame, "Left pupil:  " + str(left_pupil), (5, 61), cv2.FONT_HERSHEY_DUPLEX, 1, Color.black, 1)
        cv2.putText(frame, "Right pupil: " + str(right_pupil), (5, 94), cv2.FONT_HERSHEY_DUPLEX, 1, Color.black, 1)
        ## gaze tracking end

        ## yolo v4 start
        # apply object detection (물체 검출)
        bbox, label, conf = cvlib.detect_common_objects(frame)

        print(bbox, label, conf)
        # draw bounding box over detected objects (검출된 물체 가장자리에 바운딩 박스 그리기)
        yolo = draw_bbox(frame, bbox, label, conf, write_conf=True)
        ## yolo v4 end

        if isVideo:
            frame, angles = hpd.process_image(frame)
            if frame is None:
                break
            else:
                out.write(frame, yolo)
        else:
            # frame = cv2.flip(frame, 1)
            frame, angles = hpd.process_image(frame)

            # Display the resulting frame
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                headpose.t.summary()
                break

if __name__ == '__main__':
    # gaze tracking parameter
    gaze = GazeTracking()
    webcam = cv2.VideoCapture(0)
    # headpose detection parameter
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', metavar='FILE', dest='input_file', default=None,
                        help='Input video. If not given, web camera will be used.')
    parser.add_argument('-o', metavar='FILE', dest='output_file', default=None, help='Output video.')
    parser.add_argument('-wh', metavar='N', dest='wh', default=[720, 480], nargs=2, help='Frame size.')
    parser.add_argument('-lt', metavar='N', dest='landmark_type', type=int, default=1, help='Landmark type.')
    parser.add_argument('-lp', metavar='FILE', dest='landmark_predictor',
                        default='../Headpose_Detection/model/shape_predictor_68_face_landmarks.dat',
                        help="Landmark predictor data file.")
    # headpose detection parameter를 dict 사전형태로 모은다.
    args = vars(parser.parse_args())

    merge_detection(
        gaze=gaze,
        webcam=webcam,
        args=args
    )