import datetime
import webbrowser
import os
import wikipedia
import pyautogui
import pywhatkit
import psutil
from google import genai
import requests

def get_time() -> str:
    """Returns the current local time."""
    now = datetime.datetime.now()
    return f"The time is {now.strftime('%I:%M %p')}"

def open_website(url: str) -> str:
    """Opens a specific URL in the web browser. Input must be a full https URL."""
    webbrowser.open(url)
    return f"Successfully opened {url}"

def search_wikipedia(query: str) -> str:
    """Searches Wikipedia for a summary of a requested topic."""
    try:
        return wikipedia.summary(query, sentences=2)
    except wikipedia.exceptions.DisambiguationError:
        return "There are too many results for that query. Please be more specific."
    except wikipedia.exceptions.PageError:
        return "I could not find any results for that on Wikipedia."

def open_application(app_name: str) -> str:
    """Opens local system applications. App name should be 'notepad' or 'calculator'."""
    if "notepad" in app_name.lower():
        os.system("notepad")
        return "Notepad opened."
    elif "calc" in app_name.lower():
        os.system("calc")
        return "Calculator opened."
    return "Application not configured."

def close_active_window() -> str:
    """Closes the currently active window on the user's screen."""
    pyautogui.hotkey('alt', 'f4')
    return "Active window closed."

def play_youtube_video(song_name: str) -> str:
    """Searches YouTube and automatically plays a requested song or video."""
    pywhatkit.playonyt(song_name)
    return f"Now playing {song_name} on YouTube."

def control_system(action: str) -> str:
    """Controls system media and power. The action parameter must be exactly one of the following strings: 'pause', 'play', 'mute', 'volume up', 'volume down', 'clear'."""
    if action in ["pause", "play"]:
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
    return f"System {action} command executed."

def get_system_stats() -> str:
    """Gets the computer's real-time CPU percentage, RAM percentage, and battery status."""
    cpu_usage = psutil.cpu_percent(interval=0.5)
    ram_usage = psutil.virtual_memory().percent
    battery = psutil.sensors_battery()
    
    response = f"CPU usage: {cpu_usage}%, RAM usage: {ram_usage}%."
    if battery:
        status = "charging" if battery.power_plugged else "not charging"
        response += f" Battery: {battery.percent}%, {status}."
    return response

def take_note(note_text: str, filename: str) -> str:
    """Saves a text note to a local file. The filename MUST end with .txt."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(note_text)
    return f"I have successfully saved your note as {filename}."

def analyze_screen(question: str) -> str:
    """Takes a screenshot of the user's current computer screen and answers a question about it. Use this when the user asks you to look at their screen."""
    screenshot = pyautogui.screenshot()
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=[f"Look at this screenshot and answer: {question}. Keep it to 1 or 2 concise sentences.", screenshot]
        )
        return response.text.replace("*", "").replace("#", "")
    except Exception as e:
        return f"Failed to analyze screen: {str(e)}"

def get_weather(city: str) -> str:
    """Gets the current real-time weather conditions and temperature for a specified city."""
    try:
        response = requests.get(f"https://wttr.in/{city}?format=%C+%t")
        if response.status_code == 200:
            return f"The current weather in {city} is {response.text.strip()}."
        else:
            return f"Could not locate weather data for {city}."
    except Exception as e:
        return f"Failed to connect to weather service: {str(e)}"