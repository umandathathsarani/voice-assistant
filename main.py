import sys
import threading
import customtkinter as ctk
from modules.speech import speak, listen
import config
from modules.ai import ask_ai

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class UmoraGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(f"{config.ASSISTANT_NAME} System Terminal")
        self.geometry("700x500")
        
        self.textbox = ctk.CTkTextbox(self, width=650, height=400, font=("Consolas", 14))
        self.textbox.pack(pady=20)
        self.textbox.configure(state="disabled")
        
        self.status_label = ctk.CTkLabel(self, text="Initializing...", font=("Consolas", 16, "bold"), text_color="#00FF00")
        self.status_label.pack(pady=5)
        
        threading.Thread(target=self.run_core_loop, daemon=True).start()

    def log_to_screen(self, role, message):
        self.textbox.configure(state="normal")
        self.textbox.insert("end", f"[{role}]: {message}\n\n")
        self.textbox.see("end")
        self.textbox.configure(state="disabled")

    def update_status(self, status, color="#00FF00"):
        self.status_label.configure(text=status, text_color=color)

    def run_core_loop(self):
        welcome_text = f"Hello, I am {config.ASSISTANT_NAME}. My advanced AI routing system is online."
        self.log_to_screen("SYSTEM", welcome_text)
        speak(welcome_text)
        
        while True:
            self.update_status("Listening...", "#00FFFF")
            command = listen()
            
            if not command:
                continue
                
            self.log_to_screen("USER", command)
            self.update_status("Processing...", "#FFA500")
            
            if "goodbye" in command or "exit" in command:
                self.log_to_screen(config.ASSISTANT_NAME.upper(), "Goodbye! Shutting down now.")
                speak("Goodbye! Shutting down now.")
                self.quit()
                sys.exit()
                
            ai_response = ask_ai(command)
            self.log_to_screen(config.ASSISTANT_NAME.upper(), ai_response)
            speak(ai_response)

if __name__ == "__main__":
    app = UmoraGUI()
    app.mainloop()