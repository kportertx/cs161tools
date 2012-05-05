#! /usr/bin/python

import sys, os

if len(sys.argv) < 2:
    print "Requires 2 features, the output if everthing from feature 1 that is not in feature 2"
    print "Example: difference.py feature1 feature2"
    exit()

feat1 = sys.argv[1]
feat2 = sys.argv[2]

if not (os.path.isfile(feat1) and os.path.isfile(feat2)):
    print "feature1 and feature2 must both be a file"

f1 = open(feat1, 'r')
f2 = open(feat2, 'r')

fset1 = set(f1.readlines())
fset2 = set(f2.readlines())

f1.close()
f2.close()

rset = fset1 - fset2

result = sorted(list(rset))

for r in result:
    print r.strip()

