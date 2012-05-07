#! /usr/bin/python

import sys, os

if len(sys.argv) < 2:
    print "Need to pass a directory"
    print "Example: intersect.py PathToSamples"
    exit()

path = sys.argv[1]
ls = os.listdir(path)

set1 = None
for file_name in ls:
    file_name = path + "/" + file_name
    if os.path.isfile(file_name) and os.path.getsize(file_name) > 300:
        f = open(file_name, 'r')
        if set1 is None:
            set1 = set(f.readlines())
        else:
            set1 &= set(f.readlines())
            
        f.close()

lines = sorted(list(set1))
for l in lines:
    print l.strip()

