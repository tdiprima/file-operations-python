# Loop through the files in two directories, calculate the SHA-1 checksum
# (or any other checksum you prefer) using the subprocess module to execute
# the shasum command, and then compare the checksums to find matches.

import os
import subprocess


def calculate_sha1_checksum(file_path):
    try:
        # Execute the 'shasum' command and capture its output
        result = subprocess.run(['shasum', file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        # Parse the output to extract the checksum
        checksum = result.stdout.strip().split()[0]
        return checksum
    except subprocess.CalledProcessError:
        return None


def find_matching_files(directory1, directory2):
    # Get a list of files in each directory
    files1 = os.listdir(directory1)
    files2 = os.listdir(directory2)

    # Create dictionaries to store checksums for each directory
    checksums1 = {}
    checksums2 = {}

    # Calculate checksums for files in the first directory
    for file1 in files1:
        file1_path = os.path.join(directory1, file1)
        checksum = calculate_sha1_checksum(file1_path)
        if checksum:
            checksums1[file1] = checksum

    # Calculate checksums for files in the second directory
    for file2 in files2:
        file2_path = os.path.join(directory2, file2)
        checksum = calculate_sha1_checksum(file2_path)
        if checksum:
            checksums2[file2] = checksum

    # Find matching checksums
    # matching_checksums = set(checksums1.values()) & set(checksums2.values())

    # Find matching file names based on matching checksums
    matching_files = []
    for file1, checksum1 in checksums1.items():
        for file2, checksum2 in checksums2.items():
            if checksum1 == checksum2:
                matching_files.append((file1, file2))
                # TODO: Remove matching file from folder2
                # os.remove(os.path.join(directory2, file2))
                # print(f"Removed {file2} from {directory2}")

    return matching_files


if __name__ == "__main__":
    directory1 = "/path/to/directory1"
    directory2 = "/path/to/directory2"

    matching_files = find_matching_files(directory1, directory2)

    if matching_files:
        print("Matching files:")
        for file1, file2 in matching_files:
            print(f"{file1} in {directory1} matches {file2} in {directory2}")
            # print("Match:", file1, directory1, " matches ", file2, directory2)
    else:
        print("No matching files found.")
