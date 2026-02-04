import os
from dotenv import load_dotenv

import google.generativeai as genai

# 1. Configure the API
load_dotenv()


def generate_code(template, prompt):

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Please set the GEMINI_API_KEY environment variable.")

    genai.configure(api_key=api_key)

    # 2. Initialize the model (Gemini 1.5 Flash is fast and great for code)
    model = genai.GenerativeModel('gemma-3-27b-it')



    # We use a 'System Instruction' style prompt to ensure it only gives us code
    full_prompt = (
        f"Use this PRD as a template for the new feature described below. Output a json style response that follows the structure of the template:\n\n"
        f"Template: \n\n{template}\n\n"
        f"New Feature Description: \n\n{prompt}\n\n"
    )
    
    try:
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"Error during AI generation: {str(e)}"

if __name__ == "__main__":
    print("--- Gemini Python Code Generator ---")
    # user_input = input("What should the script do? ")
    
    print("\nGenerating code...\n")
    test_template = '{"title": "example"}'
    test_prompt = "A feature that lets users upload profile pictures."
    print(generate_code(test_template, test_prompt))