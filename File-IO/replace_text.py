import os

def replace_text_in_file(file_path, old_text, new_text):
    """
    Replaces old_text with new_text in the specified files.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        
        # Replace the old text with the new text
        new_content = content.replace(old_text, new_text)
        
        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.write(new_content)
        print(f"Replaced text in: {file_path}")
    
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def process_directory(directory, old_text, new_text, skip_folders):
    """
    Walk through all files in the directory and subdirectories,
    and replace occurrences of old_text with new_text, skipping certain folders.
    """
    for root, dirs, files in os.walk(directory):
        # Skip specific directories
        dirs[:] = [d for d in dirs if d not in skip_folders]

        for file_name in files:
            file_path = os.path.join(root, file_name)
            replace_text_in_file(file_path, old_text, new_text)

if __name__ == "__main__":
    # Define the directory to start from (current directory)
    start_directory = os.getcwd()
    
    # TODO: Define the text to replace
    old_string = ""
    new_string = ""
    
    # Folders to skip
    skip_directories = {".idea", ".git", "node_modules"}
    
    # Process all files in the directory and its subdirectories
    process_directory(start_directory, old_string, new_string, skip_directories)
    print("Text replacement completed.")
