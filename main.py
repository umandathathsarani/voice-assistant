import sys
import threading
import customtkinter as ctk
from modules.speech import speak, listen
import config
from modules.ai import ask_ai

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class UmoraGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(f"{config.ASSISTANT_NAME} Core System")
        self.geometry("900x600")
        
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.sidebar = ctk.CTkFrame(self, width=220, corner_radius=0)
        self.sidebar.grid(row=0, column=0, rowspan=2, sticky="nsew")
        self.sidebar.grid_rowconfigure(4, weight=1)
        
        self.logo_label = ctk.CTkLabel(self.sidebar, text=config.ASSISTANT_NAME.upper(), font=ctk.CTkFont(size=28, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(30, 10))
        
        self.status_label = ctk.CTkLabel(self.sidebar, text="Status: Booting...", font=ctk.CTkFont(size=15), text_color="#00FF00")
        self.status_label.grid(row=1, column=0, padx=20, pady=10)
        
        self.activity_bar = ctk.CTkProgressBar(self.sidebar, mode="indeterminate")
        self.activity_bar.grid(row=2, column=0, padx=20, pady=20)
        self.activity_bar.set(0)
        
        self.textbox = ctk.CTkTextbox(self, font=("Consolas", 15), corner_radius=10, wrap="word")
        self.textbox.grid(row=0, column=1, padx=20, pady=(20, 0), sticky="nsew")
        self.textbox.configure(state="disabled")
        
        self.entry_frame = ctk.CTkFrame(self, corner_radius=10)
        self.entry_frame.grid(row=1, column=1, padx=20, pady=20, sticky="ew")
        self.entry_frame.grid_columnconfigure(0, weight=1)
        
        self.entry = ctk.CTkEntry(self.entry_frame, placeholder_text="Awaiting voice command or type here...", font=("Consolas", 15))
        self.entry.grid(row=0, column=0, padx=(15, 10), pady=15, sticky="ew")
        self.entry.bind("<Return>", self.handle_text_input)
        
        self.send_button = ctk.CTkButton(self.entry_frame, text="Send", width=80, font=ctk.CTkFont(weight="bold"), command=self.handle_text_input)
        self.send_button.grid(row=0, column=1, padx=(0, 15), pady=15)
        
        threading.Thread(target=self.run_core_loop, daemon=True).start()

    def log_to_screen(self, role, message):
        self.textbox.configure(state="normal")
        self.textbox.insert("end", f"[{role}]: {message}\n\n")
        self.textbox.see("end")
        self.textbox.configure(state="disabled")

    def update_status(self, status, color="#00FF00", animate=False):
        self.status_label.configure(text=f"Status: {status}", text_color=color)
        if animate:
            self.activity_bar.start()
        else:
            self.activity_bar.stop()
            self.activity_bar.set(0)

    def process_command(self, command):
        self.log_to_screen("USER", command)
        self.update_status("Processing", "#FFA500", animate=True)
        
        if "goodbye" in command or "exit" in command:
            self.log_to_screen(config.ASSISTANT_NAME.upper(), "Goodbye! Shutting down now.")
            speak("Goodbye! Shutting down now.")
            self.quit()
            sys.exit()
            
        ai_response = ask_ai(command)
        self.log_to_screen(config.ASSISTANT_NAME.upper(), ai_response)
        speak(ai_response)
        
        self.update_status("Listening", "#00FFFF", animate=True)

    def handle_text_input(self, event=None):
        command = self.entry.get().strip()
        if command:
            self.entry.delete(0, "end")
            threading.Thread(target=self.process_command, args=(command,), daemon=True).start()

    def run_core_loop(self):
        welcome_text = f"Hello, I am {config.ASSISTANT_NAME}. How can I help you today?"
        self.log_to_screen("SYSTEM", welcome_text)
        speak(welcome_text)
        
        while True:
            self.update_status("Listening", "#00FFFF", animate=True)
            command = listen()
            
            if not command:
                continue
                
            self.process_command(command)

if __name__ == "__main__":
    app = UmoraGUI()
    app.mainloop()