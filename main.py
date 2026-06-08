import sys
from modules.speech import speak, listen
import config
from modules.actions import get_time, open_website, search_wikipedia, open_application, close_active_window, play_youtube_video
from modules.ai import ask_ai

def main():
    speak(f"Hello, I am {config.ASSISTANT_NAME}. Your hybrid voice system is online.")
    
    while True:
        command = listen()
        
        if not command:
            continue
            
        print(f"You said: {command}")
        
        if "goodbye" in command or "exit" in command:
            speak("Goodbye! Shutting down now.")
            sys.exit()
            
        elif "time" in command:
            current_time = get_time()
            speak(f"The time is {current_time}")
            
        elif "play" in command:
            song = command.replace("play", "").strip()
            speak(f"Playing {song} on YouTube.")
            play_youtube_video(song)
            
        elif "open google" in command:
            speak("Opening Google.")
            open_website("https://www.google.com")
            
        elif "open youtube" in command:
            speak("Opening YouTube.")
            open_website("https://www.youtube.com")
            
        elif "close window" in command or "close this" in command:
            speak("Closing window.")
            close_active_window()
            
        elif "open notepad" in command:
            speak("Opening Notepad.")
            open_application("notepad")
            
        elif "open calculator" in command:
            speak("Opening Calculator.")
            open_application("calculator")
            
        elif "wikipedia" in command:
            speak("Searching Wikipedia...")
            query = command.replace("wikipedia", "").strip()
            result = search_wikipedia(query)
            speak(result)
            
        else:
            ai_response = ask_ai(command)
            speak(ai_response)

if __name__ == "__main__":
    main()