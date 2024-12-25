import os
import sys

filepath = sys.argv[1]


def starts_with(line, thing):
    if line.startswith(thing):
        print(line)


def not_starts_with(line, thing):
    if not line.startswith(thing):
        print(line)


def thing_in(line, thing):
    if thing in line:
        print(line)


def thing_not_in(line, thing):
    if thing not in line:
        print(line)


def count_args(line):
    # Analyzing functions
    if line.startswith("function"):
        counter = line.count(',')
        # num parms, line
        print(counter + 1, line)


def replace_str(str1, arr):
    for i in arr:
        str1 = str1.replace(i, '')
    print(str1)


if __name__ == '__main__':
    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    thing = "princeton.edu"
    #  // eslint-disable-line prefer-const
    arr = ["// eslint-disable-next-line no-unused-vars", "// eslint-disable-next-line no-undef",
           "// eslint-disable-line no-unused-vars", "// eslint-disable-line no-undef"]

    with open(filepath) as fp:
        for line in fp:
            replace_str(line.strip(), arr)
            # count_args(line.strip())
            # thing_in(line.strip(), thing)
            # thing_not_in(line.strip(), thing)
            # starts_with(line.strip(), thing)
            # not_starts_with(line.strip(), thing)

exit(0)
