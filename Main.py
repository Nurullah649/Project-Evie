from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import date_information
r=sr.Recognizer()

def response(voice):
    if "sesimi alıyor musun" in voice:
        speak("Evet Alıyorum Nurullah")
    if "bugün" and "tarih" in voice:
        speak(date_information.tarih_str)
def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio=r.listen(source)
        voice=""
        try:
            voice=r.recognize_google(audio,language="tr-TR")
        except sr.UnknownValueError:
            print("Asistan anlayamadı")
        except sr.RequestError:
            print("Asistan : Sistem çalışmıyor")
        return voice

def speak(string):
    tts=gTTS(text=string,lang="tr",slow=False)
    file="Evie_voice.mp3"
    tts.save(file)
    playsound(file)

#speak("Hello")
while True:
    voice = record()
    if voice != "":
        voice = voice.lower()
        print(voice)
        response(voice)

