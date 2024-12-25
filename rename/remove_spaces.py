import os

for f in os.listdir("."):
    r = f.replace(" ", "_")
    if r != f:
        print(r)
        # os.rename(f, r)
