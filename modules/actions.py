import datetime
import webbrowser
import os
import wikipedia
import pyautogui
import pywhatkit

def get_time():
    now = datetime.datetime.now()
    return now.strftime("%I:%M %p")

def open_website(url):
    webbrowser.open(url)
    return "Opening website"

def search_wikipedia(query):
    try:
        results = wikipedia.summary(query, sentences=2)
        return results
    except wikipedia.exceptions.DisambiguationError:
        return "There are too many results for that query."
    except wikipedia.exceptions.PageError:
        return "I could not find any results for that."

def open_application(app_name):
    if "notepad" in app_name:
        os.system("notepad")
        return "Opening Notepad"
    elif "calculator" in app_name:
        os.system("calc")
        return "Opening Calculator"
    else:
        return "Application not configured."

def close_active_window():
    pyautogui.hotkey('alt', 'f4')
    return "Closing active window"

def play_youtube_video(song_name):
    pywhatkit.playonyt(song_name)
    return f"Playing {song_name} on YouTube"

def control_system(action):
    if action == "pause" or action == "play":
        pyautogui.press("playpause")
    elif action == "mute":
        pyautogui.press("volumemute")
    elif action == "volume up":
        for _ in range(5):
            pyautogui.press("volumeup")
    elif action == "volume down":
        for _ in range(5):
            pyautogui.press("volumedown")
    elif action == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')