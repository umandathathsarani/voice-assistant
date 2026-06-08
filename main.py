import sys
from modules.speech import speak, listen
import config
from modules.actions import get_time, open_website

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
            
        elif "open google" in command:
            speak("Opening Google.")
            open_website("https://www.google.com")
            
        elif "hello" in command or "hi" in command:
            speak("Hello! How can I assist you today?")
            
        else:
            speak("Command not recognized.")

if __name__ == "__main__":
    main()