import json
import os

def get_user_option():
    # File setup
    folder_name = "config"  # Ensure this matches your folder name
    file_name = "settings.json"
    
    # Path logic relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, folder_name, file_name)

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