import datetime
import webbrowser
import os
import wikipedia
import pyautogui
import pywhatkit
import psutil

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

def get_system_stats():
    cpu_usage = psutil.cpu_percent(interval=0.5)
    ram_usage = psutil.virtual_memory().percent
    battery = psutil.sensors_battery()
    
    response = f"Your CPU usage is at {cpu_usage} percent, and RAM usage is at {ram_usage} percent."
    
    if battery:
        status = "charging" if battery.power_plugged else "not charging"
        response += f" Your battery is at {battery.percent} percent and is currently {status}."
        
    return response