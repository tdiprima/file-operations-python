# Reads two specified text files and prints the lines that are common to both.
def read_file(file_path):
    """
    Function to read a file and return a set of its lines
    """
    with open(file_path, 'r') as file:
        lines = set(file.read().splitlines())
    return lines


# Input file paths
file1_path = 'file1.txt'
file2_path = 'file2.txt'

# Read the contents of both files
file1_lines = read_file(file1_path)
file2_lines = read_file(file2_path)

# Find lines that are in both files
common_lines = file1_lines.intersection(file2_lines)

# Display the common lines
print("Common lines in both files:")
for line in common_lines:
    print(line)
