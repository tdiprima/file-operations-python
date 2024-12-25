# Reads an input file, removes any duplicate lines by stripping leading and trailing spaces, and then saves
# the resulting unique lines to an output file.
def remove_duplicates(input_file, output_file):
    # Create a set to store unique lines
    unique_lines = set()

    # Read the input file and remove duplicates
    with open(input_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            # Remove leading and trailing white spaces and newline characters
            cleaned_line = line.strip()
            unique_lines.add(cleaned_line)

    # Write the unique lines to the output file
    with open(output_file, 'w') as file:
        for line in unique_lines:
            file.write(line + '\n')


if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"

    remove_duplicates(input_file, output_file)

    print(f"Duplicate lines removed. Unique lines saved to {output_file}")
