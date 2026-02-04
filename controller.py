import json
import os

from functions.findFileInHierarchy import locate_file 
from functions.templateSelector import load_template_data
from functions.promptCreation import get_multiline_input
from coder import generate_code

def get_user_option():
    # # File setup
    # folder_name = "config"  # Ensure this matches your folder name
    # file_name = "settings.json"
    
    # Path logic relative to the script location
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = locate_file("settings.json", base_dir)

    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        # Access the inner dictionary
        options = data.get("taskoptions", {})

        print("--- Select a Task ---")
        for num, info in options.items():
            print(f"[{num}] {info['name']}: {info['description']}")

        while True:
            choice = input("\nEnter the number of your choice: ")
            
            if choice in options:
                selected_name = options[choice]['name']
                print(f"Confirmed: {selected_name}")
                return choice
            else:
                print("Invalid choice. Please enter a number from 1 to 5.")

    except FileNotFoundError:
        print(f"Error: {file_name} not found in the '{folder_name}' folder.")
    except json.JSONDecodeError:
        print(f"Error: Could not read JSON format in {file_name}.")

if __name__ == "__main__":
    choice = get_user_option()
    if choice:
        # 3. Load the template dictionary
        all_templates = load_template_data()
        
        # 4. Access the specific template using the user's choice
        if choice in all_templates:
            selected_template = all_templates[choice]
            
            print("\n--- Processing Selection ---")
            print(f"Document Choice: {choice}")
            # print(f"PRD: {selected_template}")
            feature_data = get_multiline_input("Enter the Feature you want to turn into a prd")
            print("\n--- CAPTURED Feature ---")
            print(feature_data)
            print("\n--- Gemini is doing its thing! ---")
            aiResult = generate_code(selected_template, feature_data)
            print("\n--- GENERATED PRD ---")
            print(aiResult)
            # Now you have access to the specific JSON data for that choice
            # e.g., selected_template['documentName'], etc.
        else:
            print(f"⚠️ No matching template found for option {choice} in pmDocuments.json")