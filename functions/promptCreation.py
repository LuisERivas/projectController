import os
def get_multiline_input(prompt_text):
    """
    Captures multiple lines of user input and returns it as a single string variable.
    """
    print(f"\n{prompt_text} (Press Enter on an empty line to finish):")
    lines = []
    while True:
        line = input("> ")
        if not line:
            break
        lines.append(line)
    
    # This joins the list into one variable and returns it to the caller
    captured_text = "\n".join(lines)
    return captured_text

# This block ensures the code below only runs if you execute THIS file directly.
if __name__ == "__main__":
    feature_data = get_multiline_input("Enter the Feature you want to turn into a prd")
    print("\n--- CAPTURED Feature ---")
    print(feature_data)