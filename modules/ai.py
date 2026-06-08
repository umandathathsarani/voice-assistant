import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

chat_session = client.chats.create(
    model='gemini-2.5-flash',
    config=types.GenerateContentConfig(
        system_instruction="You are a helpful, concise voice assistant named Umora. Keep answers to 2 sentences max."
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