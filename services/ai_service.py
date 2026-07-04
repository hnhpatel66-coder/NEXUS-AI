import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Read API Key
API_KEY = os.getenv("GEMINI_API_KEY")

print("API KEY:", API_KEY)

# Configure Gemini
genai.configure(api_key=API_KEY)

# Load Model
model = genai.GenerativeModel("gemini-2.5-flash")


class AIService:

    @staticmethod
    def ask_ai(prompt):
        try:
            response = model.generate_content(prompt)
            return response.text

        except Exception as e:

            error = str(e)

            if "429" in error:
                return (
                    "⏳ Gemini API Rate Limit Exceeded.\n\n"
                    "Please wait 30 seconds and try again."
                )

            return f"❌ {error}"