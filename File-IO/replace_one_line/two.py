#!/usr/bin/python
s = open("mount.txt").read()
s = s.replace('mickey', 'minnie')
f = open("mount.txt", 'w')
f.write(s)
f.close()
