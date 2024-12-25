# Lists all the files in the current directory, replacing spaces in filenames with underscores and printing the modified filename.
import os

for f in os.listdir("."):
    r = f.replace(" ", "_")
    if r != f:
        print(r)
        # os.rename(f, r)
