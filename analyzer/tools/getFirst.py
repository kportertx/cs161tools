#! /usr/bin/python

import sys, os

if len(sys.argv) < 3:
    print "Need to pass a src directory and a destination directory and the number of lines you want"
    print "Example: ./getFirst.py source dest 5000"
    exit()

src = sys.argv[1]
dest = sys.argv[2]
length = int(sys.argv[3])

ls = os.listdir(src)

for fname in ls:
    src_path = src + "/" + fname
    if os.path.isfile(src_path):
        if os.path.getsize(src_path) < 300:
            continue
        src_handle = open(src_path, 'r')
        dest_path = dest + "/partial_" + fname
        dest_handle = open(dest_path, 'w')
        for i, l in enumerate(src_handle.readlines()[:length]):
            dest_handle.write(l)

