import os
from dotenv import load_dotenv

import google.generativeai as genai

# 1. Configure the API
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("Please set the GEMINI_API_KEY environment variable.")

genai.configure(api_key=api_key)

# 2. Initialize the model (Gemini 1.5 Flash is fast and great for code)
model = genai.GenerativeModel('gemma-3-27b-it')

def generate_code(prompt):
    # We use a 'System Instruction' style prompt to ensure it only gives us code
    full_prompt = (
        f"You are an expert Python developer. Write clean, documented Python code "
        f"based on this request: {prompt}. Output only the code, no conversational text."
    )
    
    response = model.generate_content(full_prompt)
    return response.text

if __name__ == "__main__":
    print("--- Gemini Python Code Generator ---")
    user_input = input("What should the script do? ")
    
    print("\nGenerating code...\n")
    code_output = generate_code(user_input)
    
    print("-" * 30)
    print(code_output)
    print("-" * 30)
    
    # Optional: Save to file
    save = input("Save to output.py? (y/n): ")
    if save.lower() == 'y':
        with open("output.py", "w") as f:
            f.write(code_output)
        print("Saved to output.py!")