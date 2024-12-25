# Scans through a given directory for Python files, computes their content hash, identifies any duplicate files based on
# those hashes, and informs the user about any found duplicates.
import os
import hashlib
import subprocess
from difflib import SequenceMatcher

# Directory containing Python files
directory = "."

# Dictionary to store file hashes and their paths
file_hashes = {}

# Function to calculate a hash of a file's content
def calculate_hash(file_path):
    with open(file_path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

# Function to execute a Python script and capture its output
# def execute_script(file_path):
#     try:
#         result = subprocess.run(
#             ["python3", file_path],
#             capture_output=True,
#             text=True,
#             timeout=10  # Set a timeout for safety
#         )
#         return result.stdout.strip()  # Return the script output
#     except Exception as e:
#         return str(e)  # Return the error as output

# Analyze Python files
def analyze_files(root_dir):
    duplicates = []
    outputs = {}  # Store script outputs to identify functional duplicates

    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(subdir, file)

                # Static analysis: Calculate hash
                file_hash = calculate_hash(file_path)
                if file_hash in file_hashes:
                    duplicates.append((file_path, file_hashes[file_hash]))
                    continue
                file_hashes[file_hash] = file_path

                # Dynamic analysis: Execute the file
                # output = execute_script(file_path)
                # if output in outputs:
                #     duplicates.append((file_path, outputs[output]))
                # else:
                #     outputs[output] = file_path

    return duplicates

# Main function
if __name__ == "__main__":
    duplicates = analyze_files(directory)
    if duplicates:
        print("Found duplicate files:")
        for dup in duplicates:
            print(f"{dup[0]} is a duplicate of {dup[1]}")
    else:
        print("No duplicates found.")
