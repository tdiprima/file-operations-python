import datetime
import os


def remove_spaces(directory="."):
    """
    Replace spaces in filenames with underscores in the specified directory.
    :param directory: Directory to process (default is current directory).
    """
    for filename in os.listdir(directory):
        new_name = filename.replace(" ", "_")
        if new_name != filename:
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
            print(f"Renamed: {filename} -> {new_name}")


def rename_by_timestamp(directory="."):
    """
    Rename files in the specified directory based on their creation timestamps.
    :param directory: Directory to process (default is current directory).
    """
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            # Get creation time
            creation_time = os.path.getctime(filepath)
            timestamp = datetime.datetime.fromtimestamp(creation_time).strftime("%Y-%m-%d_%H:%M:%S")

            new_name = f"{timestamp}_{filename}"
            os.rename(filepath, os.path.join(directory, new_name))
            print(f"Renamed: {filename} -> {new_name}")


def replace_extension(directory=".", old_ext=".dat", new_ext=".dcm"):
    """
    Replace the file extension of all files in the specified directory from old_ext to new_ext.
    :param directory: Directory to process (default is current directory).
    :param old_ext: Extension to be replaced (e.g., .dat).
    :param new_ext: New extension to apply (e.g., .dcm).
    """
    for filename in os.listdir(directory):
        if filename.endswith(old_ext):
            new_name = filename[:-len(old_ext)] + new_ext
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
            print(f"Renamed: {filename} -> {new_name}")


# Example usage:
# remove_spaces("/path/to/directory")
# rename_by_timestamp("/path/to/directory")
replace_extension("/path/to/directory", ".dat", ".dcm")
