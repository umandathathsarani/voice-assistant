import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from modules import actions

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

my_tools = [
    actions.get_time,
    actions.open_website,
    actions.search_wikipedia,
    actions.open_application,
    actions.close_active_window,
    actions.play_youtube_video,
    actions.control_system,
    actions.get_system_stats,
    actions.take_note,
    actions.analyze_screen,
    actions.get_weather,
    actions.set_reminder
]

chat_session = client.chats.create(
    model='gemini-2.5-flash',
    config=types.GenerateContentConfig(
        system_instruction="You are Umora, an advanced AI voice assistant. You have been granted access to local system tools. When the user asks you to do something, USE the appropriate tool to execute the action. Keep your spoken responses to 1 brief sentence.",
        tools=my_tools,
        temperature=0.3
    )
)

def ask_ai(prompt):
    try:
        response = chat_session.send_message(prompt)
        clean_text = response.text.replace("*", "").replace("#", "")
        return clean_text
    except Exception as e:
        print(f"\n[Error Log]: {e}\n")
        return "I am having trouble connecting to my AI network right now."