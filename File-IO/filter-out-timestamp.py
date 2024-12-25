# Reads a specified text file and prints the lines that do not start with a timestamp (format HH:MM).
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
