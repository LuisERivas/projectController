import json
import os
from functions.findFileInHierarchy import locate_file

def load_template_data():
    """
    Locates pmDocuments.json dynamically and returns the 'taskoptions' dictionary.
    """
    # 1. Get the directory where this script lives to start the search
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 2. Use the imported locate_file function to find the JSON
    # It will search deep in subfolders and climb up to the controller script
    file_path = locate_file("pmDocuments.json", base_dir)

    if not file_path:
        print("Error: Could not locate 'pmDocuments.json' within the project hierarchy.")
        return {}

    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        # 3. Return the inner pmDocuments dictionary
        # Using .get() prevents a crash if the key is missing
        return data.get("pmDocuments", {})
    
    except json.JSONDecodeError:
        print(f"Error: {file_path} contains invalid JSON formatting.")
        return {}
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {}

def main():
    template = load_template_data()
    
    if template:
        print(f"✅ Data loaded successfully. Found {len(template)} template options.")
        # Example: Print the name of the first template
        if "1" in template:
            print(f"Selected Template: {template['1']['documentDescription']}")
    else:
        print("❌ No templates found or file failed to load.")

if __name__ == "__main__":
    main()