import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("API_KEY"))

# Set system instructions for the email generator
instructions = """
You are an expert email generator. Your role is to craft professional and engaging email responses.
- Always use proper formatting and structure.
- Adapt the tone of the email based on the input provided (Formal or Informal).
- Include an appropriate salutation and closing signature.
- If a recipient is specified, address them directly.
"""

# Create the model with specific system instructions
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=instructions
)

def generate_email(recipient, message, tone):
    """
    Generates an email using the Gemini API.

    Args:
        recipient (str): The recipient's name or email address.
        message (str): The user's prompt for the email content.
        tone (str): The tone of the email (Formal or Informal).

    Returns:
        str: The generated email content.
    """
    user_prompt = f"""
    Generate an email with the following details:
    - Recipient: {recipient if recipient else 'Generic'}
    - Tone: {tone}
    - Message: {message}
    """
    try:
        response = model.generate_content(user_prompt)
        return response.text
    except Exception as e:
        return f"Error generating email: {str(e)}"
