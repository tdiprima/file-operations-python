# Calculates SHA1 hashes of all files in a specified directory (including subdirectories), and
# removes any duplicates by comparing these hashes.
import os
import hashlib


def calculate_sha1(file_path):
    sha1 = hashlib.sha1()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            sha1.update(chunk)
    return sha1.hexdigest()


def remove_duplicates(directory):
    hash_dict = {}
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_hash = calculate_sha1(file_path)

            if file_hash in hash_dict:
                print(f"Removing duplicate file {file_path}, duplicate of {hash_dict[file_hash]}")
                os.remove(file_path)
            else:
                hash_dict[file_hash] = file_path
                print(f"Hashing {file_path}, SHA1: {file_hash}")


if __name__ == "__main__":
    directory = "./test_directory"  # Replace with the directory you want to check
    remove_duplicates(directory)
