# Calculates and prints the total number of files in the current directory and all its subdirectories.
from os import walk

print(sum([len(files) for (root, dirs, files) in walk('.')]))
