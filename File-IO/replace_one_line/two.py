# Reads a file named "mount.txt", replaces all occurrences of the string 'mickey' with 'minnie', and overwrites the file with the modified content.
s = open("mount.txt").read()
s = s.replace('mickey', 'minnie')
f = open("mount.txt", 'w')
f.write(s)
f.close()
