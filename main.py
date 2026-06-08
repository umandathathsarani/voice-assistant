import sys
from modules.speech import speak, listen
import config
from modules.ai import ask_ai

def main():
    speak(f"Hello, I am {config.ASSISTANT_NAME}. My advanced AI routing system is online.")
    
    while True:
        command = listen()
        
        if not command:
            continue
            
        print(f"You said: {command}")
        
        if "goodbye" in command or "exit" in command:
            speak("Goodbye! Shutting down now.")
            sys.exit()
            
        ai_response = ask_ai(command)
        speak(ai_response)

if __name__ == "__main__":
    main()