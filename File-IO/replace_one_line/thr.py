# Replaces all instances of the word "old" with the word "new" in the file "mount.txt".
import fileinput

for line in fileinput.FileInput("mount.txt", inplace=1):
    line = line.replace("old", "new")
    print(line)
