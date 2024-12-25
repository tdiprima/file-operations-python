# Updates the 'patch_w' and 'patch_h' values of the JSON object in the first line of a CSV file, and writes the updated content into a new CSV file.
import json
import os


def json_replace(first_line):
    first_line = first_line.strip('\n').replace('\"\"', '\"').replace("\"{", "{").replace("}\"", "}")
    parsed_json = json.loads(first_line)
    new_width = 200
    new_height = 200
    parsed_json['patch_w'] = new_width
    parsed_json['patch_h'] = new_height
    replacement_line = json.dumps(parsed_json)
    replacement_line = replacement_line.replace('\"', '\"\"')
    return "\"" + replacement_line + "\""


newline = os.linesep  # Defines the newline based on your OS.

source_filename = 'test.csv'
target_filename = 'newfile.csv'
source_fp = open(source_filename, 'r')
target_fp = open(target_filename, 'w')
first_row = True
for row in source_fp:
    if first_row:
        row = json_replace(row)
        first_row = False
        target_fp.write(row + newline)
    else:
        target_fp.write(row)
