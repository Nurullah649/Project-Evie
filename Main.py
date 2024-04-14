from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import date_information
from googletrans import Translator
r = sr.Recognizer()
def translate_text(text, target_language='en'):
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    print(translated.text)
    return translated.text

def response(voice):
    if "sesimi alıyor musun" in voice:
        speak("Evet Alıyorum Nurullah")
    elif "çevirir misin" in voice:
        text_to_translate = voice.replace("çevirir misin", "").strip()
        speak(translate_text(text_to_translate))
    elif "bugün" in voice and "tarih" in voice:
        speak(date_information.tarih_str)
    elif "bugün" in voice and "tarih" in voice and "günü" in voice:
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

while True:
    voice = record()
    if voice != "":
        voice = voice.lower()
        print(voice)
        response(voice)
