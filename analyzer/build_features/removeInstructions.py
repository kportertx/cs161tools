#! /usr/bin/python

import sys, os

if len(sys.argv) < 3:
    print "Need to pass a directory to remove instructions from and a directory to write to"
    print "Example: ./removeInstructions.py source dest"
    exit()

path = sys.argv[1]
dest = sys.argv[2]

ls = os.listdir(path)

for src in ls:
    src_path = path + "/" + src
    if os.path.isfile(src_path):
        if os.path.getsize(src_path) < 300:
            continue
        src_handle = open(src_path, 'r')
        dest_path = dest + "/" + src
        dest_handle = open(dest_path, 'w')
        for l in src_handle:
            s = l.strip().lower()
            if s == '' or s[0] != 'd':
                continue
            dest_handle.write(l)


