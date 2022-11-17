import speech_recognition as sr
import pyaudio

r = sr.Recognizer()

print("Running")

p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
    print(p.get_device_info_by_index(i))

# num = 0  # 외부 모니터 없이 돌릴 시,
num = 1  # 외부 모니터 연결되었을 시,

with sr.Microphone(num) as source:
    r.adjust_for_ambient_noise(source, num)  # Adjust for ambient
    print("Say something!")
    audio = r.listen(source)
print("Runnnnnn")
try:
    print("Analyzing voice data  " + r.recognize_google(audio, language='ko'))
except Exception:
    print("Something went wrong")