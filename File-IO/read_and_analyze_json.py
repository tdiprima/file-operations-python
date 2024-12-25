# Reads two JSON files, parses them, prints their content and filters objects with "Series": "I" in the second file, printing those filtered objects.
import json


def read_and_parse_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data


# File 1
filename = "sample.json"
parsed_data = read_and_parse_json(filename)

# Printing the parsed data
print(json.dumps(parsed_data, indent=4))

# File 2
filename = "sample1.json"
parsed_data = read_and_parse_json(filename)

# Filtering the parsed data for objects with "Series": "I"
series_I_objects = [obj for obj in parsed_data if obj.get("Series") == "I"]

# Printing the filtered objects
for obj in series_I_objects:
    print(obj)
