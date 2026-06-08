import speech_recognition as sr
import pyttsx3
import config

tts_engine = pyttsx3.init()
tts_engine.setProperty('rate', 175)
tts_engine.setProperty('volume', 1.0)

voices = tts_engine.getProperty('voices')
tts_engine.setProperty('voice', voices[0].id) 
## 0 --> Microsoft David (Male) 
## 1 --> Microsoft Zira (Female)

def speak(text):
    print(f"{config.ASSISTANT_NAME}: {text}")
    tts_engine.say(text)
    tts_engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    if not config.FORCE_OFFLINE:
        try:
            print("Processing (Online)...")
            text = recognizer.recognize_google(audio)
            return text.lower()
        except sr.RequestError:
            pass
        except sr.UnknownValueError:
            return ""

    try:
        print("Processing (Offline)...")
        text = recognizer.recognize_sphinx(audio)
        return text.lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""