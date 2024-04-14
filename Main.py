import os
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import date_information
from googletrans import Translator
r = sr.Recognizer()
def translate_text(text, target_language):
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    print(translated.text)
    return translated.text

def response(voice):
    if "sesimi alıyor musun" in voice:
        speak("Evet Alıyorum Nurullah")
    if "çevirir misin" in voice:
        #voice = voice.replace("çevirir misin", "").strip()
        substring = voice[voice.find("bunu")+5:voice.find("bunu")+16]
        if substring.lower() == 'ingilizceye':
            print("burda")
            text_to_translate=voice.replace("bunu ingilizceye çevirir misin","").strip()
            print(text_to_translate)
            speak(translate_text(text_to_translate,'en'))
        elif "frasızcaya" in voice:
            text_to_translate = voice.replace("frasızcaya", "").strip()
            print(text_to_translate)
            speak(translate_text(text_to_translate, 'fr'))
    if "bugün" in voice and "tarih" in voice:
        speak(date_information.tarih_str)
    elif "bugün" in voice and "tarih" in voice and "günü" or "gün" in voice:
        speak(date_information.day_tarih_str)

def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            print("Asistan anlayamadı")
        except sr.RequestError:
            print("Asistan : Sistem çalışmıyor")
        return voice

def speak(string):
    tts = gTTS(text=string, lang="tr", slow=False)
    file = "Evie_voice.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

while True:
    voice = record()
    if voice != "":
        voice = voice.lower()
        print(voice)
        response(voice)
