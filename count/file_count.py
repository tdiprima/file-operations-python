# Counts and prints the number of files in each subdirectory for a given target directory.
import os


def count_files_in_subdirectories(target_directory):
    """
    Count the number of files in each subdirectory of the given target directory.
    """
    try:
        print(f"Scanning directory: {target_directory}\n")
        for root, dirs, files in os.walk(target_directory):
            subdir = os.path.relpath(root, target_directory)
            if subdir == '.':
                subdir = "Root Directory"
            print(f"{subdir}: {len(files)} file(s)")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Set the target directory here
    target_directory = input("Enter the target directory (leave blank for current directory): ").strip()
    if not target_directory:
        target_directory = os.getcwd()

    count_files_in_subdirectories(target_directory)
