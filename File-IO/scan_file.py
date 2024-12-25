# Contains several functions that perform various operations on file data, such as scanning a file for a specific string, modifying file output, converting html references in file to JavaScript, removing JavaScript comments, slicing file data based on provided start and end strings, writing file contents on one line, finding multiple strings in a file, adding colourful JavaScript function comments, selecting some lines based on a search string, and cleaning matlab function comments.
import os
import random
import sys
from pathlib import Path


def mod(filename):
    count = 0
    with open(filename) as fp:
        for line in fp:
            line = line.strip()
            print(line)
            count += 1
            if count % 5 == 0:
                print()


def plain_old_scan(filename):
    with open(filename) as fp:
        for line in fp:
            line = line.strip()
            print("<script src=\"" + line.replace("html", "js") + "\"</script>")


def scan(filename, search_str):
    with open(filename) as fp:
        for line in fp:
            line = line.strip()
            # if line.startswith(search_str):
            if search_str in line:
                print(line)


def scan_with_line_num(filename, search_str):
    with open(filename) as myFile:
        for num, line in enumerate(myFile, 1):
            if search_str in line:
                print(str(num) + ": " + line.strip())


def rem_js_comments(filename):
    search_str = '//'
    with open(filename) as fp:
        for line in fp:
            line = line.strip()
            # if '//' not in line and '/*' not in line and '<!--' not in line and len(line) > 0:
            if search_str not in line and len(line) > 0:
                print(line)


def slicing(filename, start, end):
    """
    string[start:]
    index = animals.index('dog')
    string.split()
    """
    count = 0
    with open(filename) as fp:
        for line in fp:
            line = line.strip()
            if start in line:
                count += 1
                # start: The character at this index is included in the substring.
                # end: The character at this index is NOT included in the substring.
                start_index = line.index(start)
                end_index = line.index(end)

                # print(line[start_index:end_index])

                # make array, print without newline
                print("'" + line[start_index:end_index] + "', ", end='')
    print('count:', count)


def select_part_of_line(filename, search_str):
    count = 0
    with open(filename) as fp:
        for line in fp:
            line = line.strip()
            if search_str in line:
                count += 1
                # start: The character at this index is included in the substring.
                # end: The character at this index is NOT included in the substring.
                start_index = line.index(search_str)
                end_index = line.index("\">")
                print('open', line[start_index:end_index])
    print('count:', count)


def write_on_one_line(filename):
    with open(filename) as fp:
        for line in fp:
            line = line.strip()
            print("\"" + line + "\" ", end='')


def find_many_things(filename, this_list):
    with open(filename) as fp:
        for line in fp:
            line = line.strip()
            for i, e in reversed(list(enumerate(this_list))):
                if e in line:
                    # print(e)
                    # make array, print without newline
                    print("'" + e + "', ", end='')
                    this_list.pop(i)
                    break


def js_fun_comments(filename):
    colour = ["#ff00cc", "orange", "#ccff00", "lime", "cyan", "deeppink", "#997fff"]
    search_str = 'function'
    with open(filename) as fp:
        for line in fp:
            line = line.strip()
            if search_str in line:
                number = random.randint(0, 5)
                print(line)
                # print('console.log("%c' + line + '", "color: ' + colour[number] + '");')
                print('console.log("%c' + line[line.index(search_str) + len(search_str) + 1: line.index(
                    '(')] + '", "color: ' + colour[number] + '");')
            else:
                print(line)


def select_some(filename, search_str):
    # "commit"
    count = 0
    web_page = "https://github.com/tdiprima/multi-viewer/commit/"
    with open(filename) as fp:
        for line in fp:
            line = line.strip()
            if search_str in line:
                count += 1
                # Select a handful of them (or two)
                if count % 20 == 0 or count == 1:
                    print('open ' + web_page + line[7: 14])


def clean_matlab_fun(filename):
    count = 0
    with open(filename) as fp:
        for line in fp:
            line = line.strip()
            if line.startswith("%"):
                count = count + 1
            else:
                print(line)


if __name__ == "__main__":
    scan("path", "something")

exit(0)
