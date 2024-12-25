# Read a file, search each line using a regular expression pattern, and replace the matched pattern with an empty string
import re


def process_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            # Match one or more digits (\d+), followed by a period (\.),
            # and a space (\s) at the beginning of the line (^).
            pattern = r'^\d+\.\s'

            # Use re.sub to replace the matched pattern with an empty string
            processed_line = re.sub(pattern, '', line)

            # Print the processed line
            print(processed_line, end='')


# Replace 'filename.txt' with the actual name of your file
process_file('filename.txt')
