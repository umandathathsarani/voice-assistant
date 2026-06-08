import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def ask_ai(prompt):
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=f"You are a helpful, concise voice assistant named Jarvis. Keep answers to 2 sentences max. User says: {prompt}"
        )
        clean_text = response.text.replace("*", "").replace("#", "")
        return clean_text
    except Exception as e:
        print(f"\n[Error Log]: {e}\n")
        return "I am having trouble connecting to my AI network right now."