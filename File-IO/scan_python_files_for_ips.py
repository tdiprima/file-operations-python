import os
import re
import logging

# Configure logging
logging.basicConfig(
    filename='ip_scan_log.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
)

# Define regex pattern for IP addresses
ip_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'

def find_ips_in_file(file_path):
    """Check if a file contains an IP address."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            ip_matches = re.findall(ip_pattern, content)
            if ip_matches:
                logging.info(f"File: {file_path} contains IP addresses: {', '.join(ip_matches)}")
    except Exception as e:
        logging.error(f"Error reading file {file_path}: {e}")

def iterate_python_files(root_folder):
    """Iterate through all Python files in subfolders."""
    for subdir, _, files in os.walk(root_folder):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(subdir, file)
                find_ips_in_file(file_path)

if __name__ == '__main__':
    root_directory = input("Enter the root directory to scan: ")
    iterate_python_files(root_directory)
    print("Scan complete. Check 'ip_scan_log.log' for details.")
