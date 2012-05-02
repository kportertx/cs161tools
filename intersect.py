#! /usr/bin/python

import sys, os

if len(sys.argv) < 2:
    print "Need to pass a directory"
    print "Example: intersect.py PathToSamples"
    exit()

path = sys.argv[1]
ls = os.listdir(path)

set2 = None
set1 = None
for file_name in ls:
    set1 = set()
    file_name = path + "/" + file_name
    if os.path.isfile(file_name):
        if os.path.getsize(file_name) < 300:
            continue
        f = open(file_name, 'r')
        for l1 in f:
            set1.add(l1.strip())
        if set2 is None:
            set2 = set1
        else:
            tmp = set2 & set1
            set2 = tmp

lines = sorted(list(set2))
for l in lines:
    print l

