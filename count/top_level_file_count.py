# Counts and prints the number of files in each top-level subdirectory of a given directory, with the directory to be scanned specified by user input.
import os


def count_files_in_top_level_subdirectories(target_directory):
    """
    Count the number of files in each top-level subdirectory of the given target directory.
    """
    try:
        print(f"Scanning top-level subdirectories of: {target_directory}\n")

        # Get the list of all subdirectories in the target directory
        for item in os.listdir(target_directory):
            item_path = os.path.join(target_directory, item)

            # Check if the item is a directory
            if os.path.isdir(item_path):
                # Count files in the subdirectory
                file_count = len([f for f in os.listdir(item_path) if os.path.isfile(os.path.join(item_path, f))])
                print(f"{item}: {file_count} file(s)")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Set the target directory here
    target_directory = input("Enter the target directory (leave blank for current directory): ").strip()
    if not target_directory:
        target_directory = os.getcwd()

    count_files_in_top_level_subdirectories(target_directory)
