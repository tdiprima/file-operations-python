# This script will print the lines that don't start with timestamps like "5:11" or "13:15".
import re

def does_not_start_with_timestamp(line):
    pattern = r'^\d{1,2}:\d{2}'
    return not re.match(pattern, line)

def main():
    with open('file_path.txt', 'r') as file:
        for line in file:
            if does_not_start_with_timestamp(line):
                print(line, end='')

if __name__ == '__main__':
    main()
