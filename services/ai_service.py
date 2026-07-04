import os
import google.generativeai as genai
from dotenv import load_dotenv

# ==========================================
# LOAD ENVIRONMENT
# ==========================================

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "❌ GEMINI_API_KEY not found in .env"
    )

genai.configure(api_key=API_KEY)

# ==========================================
# GEMINI MODEL
# ==========================================

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


# ==========================================
# AI SERVICE
# ==========================================

class AIService:

    @staticmethod
    def generate_response(prompt: str) -> str:
        """
        Main AI Response Method
        """

        try:

            response = model.generate_content(
                prompt
            )

            if hasattr(response, "text"):
                return response.text

            return "⚠ Empty response."

        except Exception as e:

            error = str(e)

            if "429" in error:

                return (
                    "⏳ Gemini API Rate Limit Exceeded.\n\n"
                    "Please wait a moment and try again."
                )

            return f"❌ {error}"

    # ======================================
    # BACKWARD COMPATIBILITY
    # ======================================

    @staticmethod
    def ask_ai(prompt: str) -> str:
        """
        Old Method Support
        """
        return AIService.generate_response(prompt)