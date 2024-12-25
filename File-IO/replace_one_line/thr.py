#!/usr/bin/python
import fileinput

for line in fileinput.FileInput("mount.txt", inplace=1):
    line = line.replace("old", "new")
    print(line)
