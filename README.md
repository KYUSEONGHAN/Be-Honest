# Be-Honest
- AI를 활용한 온라인 시험 컨닝 감독 프로그램

## 최종 결과 화면
![스크린샷 2022-11-20 오후 5 56 41](https://user-images.githubusercontent.com/82144756/224476811-41810059-9369-4bbf-b500-b498b4b11eff.png)
- 부정행위 물품 중 하나인 스마트폰이 시험 중 인식이되서 감독관 sns에 bot이 자동으로 스크린샷과 내용을 DM 보낸 상황이다.

## 성과
- [CEDC 2022(Creative Engineering Design Competition)](https://ire-asia.org/ire/cedc/): `은상`
- [2022 START-UP BATTLE GROUNDS](https://cip.chungbuk.ac.kr/post/155): `장려상`
- 충북대학교 정보통신공학부 졸업작품

## 개발 의도
- 코로나 시국인 요즘, 대다수의 학교와 기업에서 비대면 시험을 진행하고 있는 상황이다.
- 하지만, 비대면 시험의 허술한점을 악용해 부정행위를 저지르는 사람들이 많아 대다수의 시험 감독관이 골치아파한다.

## 개발 목적
- AI 컨닝 감독 프로그램을 만들어 다수의 응시자가 시험을 볼 때, 감독관이 화면을 안봐도 부정행위를 검출할 수 있도록 개발.
- AI가 빠르고 정확하게 온라인 시험에서 부정행위를 검출할 수 있도록한다.
- 시험 감독관의 SNS을 연동해 알림을 보내는 BOT을 개발한다.
- 시험 감독관은 화면을 보지않고 다른 일을 하고있어도 되며, 부정행위가 의심되는 응시자들의 화면 스크린샷 사진과 해당 응시자 정보를 자동으로 SNS로 전달받는다.
- 감독관이 해당 메시지를 보고 응시자에게 경고를 하거나, 시험을 강제종료 시킨다.

## 참여 인원 및 역할
- 참여 인원: 3명
- 역할: 팀장(기획, BE, ML)
    - BE
        - Flask + MariaDB 서버 구축
        - Slack 연동 및 Bot 구축
        - AI 실시간 부정행위 검출 기능 개발
    - ML
        - YOLO V4, GazeTracking, DeepFace, Headpose-Detection, LBP 알고리즘 연동 및 최적화

## 개발 스택
- Programming Language
    - Python3, Jinja2, HTML, CSS3, JavaScript
- Framework
    - Flask
- Server
    - MariaDB
- Algorithm
    - YOLO V4, DeepFace, LBP, GazeTracking, Headpose-Detection
- Library
    - JQuery, Open-CV, Pyaudio, speech_recognition, psutill, pyautogui, time
- Tolling
    - Slack, Github

## Program Logic
![image](https://user-images.githubusercontent.com/82144756/224476078-418036fa-2ca3-4806-a151-a619feee9f68.png)

## AI가 인식하는 부정행위 목록
1. 웹캠에 핸드폰, 책 등이 인식되는 경우
2. 웹캠에 인식되는 사람이 한명이 아닌 경우
3. 웹캠에 응시자가 아닌 사람이 인식되는 경우
4. 웹캠에 응시자의 동공이 컴퓨터 화면 영역 밖을 바라보는게 인식되는 경우
5. 웹캠에 응시자의 고개 각도가 화면 영역을 넘어서는게 인식되는 경우
6. 응시자 컴퓨터에 외부 모니터가 연결되어있는 경우
7. 응시자 컴퓨터에 에어팟, 패드 등이 연결되어 있는 경우
8. 응시자 컴퓨터에 부정행위가 의심되는 어플이 활성화되있는 경우
9. 음성이 인식되는 경우

## 각 기능별 간단 설명
### 1번, 2번
![image](https://user-images.githubusercontent.com/82144756/224476973-6c1261d0-2792-41fe-b991-6e9d4b396c68.png)
![image](https://user-images.githubusercontent.com/82144756/224476976-771a436d-7c79-46ca-8aa8-b39cfb66a5f7.png)
- `YOLO V4 알고리즘 사용` [https://arxiv.org/pdf/2004.10934v1.pdf](https://arxiv.org/pdf/2004.10934v1.pdf)
- YOLO V4 알고리즘을 사용하여 사람 수, 부정행위에 의심되는 물품들 실시간 인식 (ex: 책, 종이, 모니터, 에어팟 등)
- 에어팟은 기존 YOLO V4에 학습된 데이터셋에 없으므로 커스텀 데이터셋을 직접 제작해 모델에 학습.

### 3번
![image](https://user-images.githubusercontent.com/82144756/224477238-371ce1ce-ff27-4257-ae0f-adedeae81adb.png)
![image](https://user-images.githubusercontent.com/82144756/224477244-2f088070-db35-460b-bd83-17d6cf83fd89.png)
- `DeepFace & LBP 알고리즘 사용`
- DeepFace: [https://www.cs.toronto.edu/~ranzato/publications/taigman_cvpr14.pdf](https://www.cs.toronto.edu/~ranzato/publications/taigman_cvpr14.pdf)
- LBP: [https://www.academia.edu/75025763/A_texture_descriptor_BackGround_Local_Binary_Pattern_BGLBP_](https://www.academia.edu/75025763/A_texture_descriptor_BackGround_Local_Binary_Pattern_BGLBP_)
-  회원가입할 때 수험표를 입력 받음 -> 수험표 사진을 저장.
- DeepFace와 LBP 알고리즘을 사용하여 수험표 사진과 화면에 인식되는 얼굴을 비교하여 응시자 본인인지 대리인인지 체크

### 4번
![image](https://user-images.githubusercontent.com/82144756/224477314-966016a5-5b3d-4ca0-8963-9dcfb6ff20d1.png)
- `GazeTracking 알고리즘 사용`: [https://arxiv.org/abs/2009.01270](https://arxiv.org/abs/2009.01270)
- GazeTracking 알고리즘을 사용하여 각 동공의 x, y 위치와 어디를 바라보는지를 인식한 후, 모니터 경계영역(Bounding Box)를 넘어서는지 체크
    - if 경계상자(Bounding Box)를 넘어섰다. -> 부정행위 의심

### 5번
![image](https://user-images.githubusercontent.com/82144756/224477369-a3638b48-97c9-4f13-b094-7af0f35fe5c9.png)
- 부정행위는 눈동자를 다른곳으로 보는것 뿐만이아닌, 고개를 돌려 컨닝하는 경우도 있으므로 고개각도를 검출할 필요성이 있다.
- Headpose-Detection 알고리즘을 이용하여 실시간으로 고개각도 x, y, z 좌표를 추출 -> x, y, z 좌표가 일정 영역(Bounding Box)를 넘어서면 부정행위 의심 

### 6번
- `wxPython 라이브러리 사용`
- 듀얼모니터일시, true를 반환 -> 시험 감독관한테 자동으로 메시지 보냄. 
- 듀얼모니터가 아니면, false를 반환

### 7번
- `Pyaudio 라이브러리 사용`
- 컴퓨터와 연결된 전자기기를 판별 할 수 있다.

### 8번
- `psutil 라이브러리 사용`
- 컴퓨터에 활성화된 어플리케이션을 알 수 있다.
- 활성 금지 어플리케이션 목록
    - 카카오톡
    - 텔레그램
    - 슬랙
    - 라인
    - 유튜브
    - 줌

### 9번
- `Pyaudio를 이용한 마이크 음성인식`

## 1번~9번 작동 샘플 이미지
![스크린샷 2022-11-21 오후 5 01 06](https://user-images.githubusercontent.com/82144756/224478033-f5c3952d-b94c-42e9-9094-d4fecd8554b3.png)