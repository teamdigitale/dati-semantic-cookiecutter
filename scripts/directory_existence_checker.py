import os

def check_directory_existence(root_dirs):
    existing_dirs = [root_dir for root_dir in root_dirs if os.path.exists(root_dir)]
    if not existing_dirs:
        print("(no files to check)Skipped")
        return False

    for root_dir in existing_dirs:
        print(f"WARNING: {root_dir} does not exist")
    return True