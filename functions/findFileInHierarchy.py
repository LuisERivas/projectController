import os

def locate_file(target_filename, start_dir, limit_script="controller.py"):
    """
    Finds a file by searching deep into subfolders and moving up the directory 
    tree until a limit script is hit. Skips .git and .env.
    """
    ignore_list = {'.env', '.git'}
    visited_dirs = set()
    current_dir = os.path.abspath(start_dir)

    def deep_search(directory):
        """Internal recursive helper for deep scanning."""
        for root, dirs, files in os.walk(directory):
            # Exclude ignored dirs in-place
            dirs[:] = [d for d in dirs if d not in ignore_list]
            
            # Log current subfolder being scanned
            rel_path = os.path.relpath(root, directory)
            if rel_path != ".":
                print(f"    [Sub-Folder] {rel_path}")

            for f in files:
                if f in ignore_list: continue
                print(f"    [Sub-File]   {f}")
                if f == target_filename:
                    return os.path.join(root, f)
        return None

    # Main Upward Loop
    while True:
        print(f"\n🔍 Searching Level: {current_dir}")
        
        try:
            entries = os.listdir(current_dir)
            for entry in entries:
                if entry in ignore_list: continue
                
                full_path = os.path.join(current_dir, entry)

                if os.path.isdir(full_path):
                    # Only search this folder if we haven't been inside it yet
                    if full_path not in visited_dirs:
                        print(f"  [Entering Folder] {entry}")
                        found = deep_search(full_path)
                        if found: return found
                        visited_dirs.add(full_path)
                else:
                    print(f"  [File]   {entry}")
                    if entry == target_filename:
                        return full_path

            # Stop if we hit the ceiling
            if limit_script in entries:
                print(f"🚩 Reached '{limit_script}'. Scope finalized.")
                break

        except PermissionError:
            print(f"  ⚠️ Access Denied: {current_dir}")

        # Move Up
        parent_dir = os.path.dirname(current_dir)
        if parent_dir == current_dir: break
        current_dir = parent_dir

    return None

if __name__ == "__main__":
    # Test the combined function
    path = locate_file("pmDocuments.json", os.path.dirname(__file__))
    print(f"\nResult: {path if path else 'Not Found'}")