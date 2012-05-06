#! /usr/bin/python

import sys, os

if len(sys.argv) < 2:
    print "Requires 2 features, the output if everthing from feature 1 that is not in feature 2"
    print "Example: difference.py feature1 feature2"
    exit()

feat1 = sys.argv[1]
feat2 = sys.argv[2]

if not (os.path.isfile(feat1) and (os.path.isfile(feat2) or os.path.isdir(feat2))):
    print "feature1 and feature2 must both be a file"

result = []
if os.path.isfile(feat2):
    f1 = open(feat1, 'r')
    f2 = open(feat2, 'r')
    
    fset1 = set(f1.readlines())
    fset2 = set(f2.readlines())

    f1.close()
    f2.close()
    
    rset = fset1 - fset2
    result = sorted(list(rset))
else:
    f1 = open(feat1, 'r')
    fset1 = set(f1.readlines())
    f1.close()
    
    ls = os.listdir(feat2)
    for file_name in ls:
        file_name = feat2 + "/" + file_name
        if os.path.isfile(file_name):
            if os.path.getsize(file_name) < 300:
                continue
            f2 = open(file_name, 'r')
            fset2 = set(f2.readlines())
            f2.close()
            rset = fset1 - fset2
            fset1 = rset
    result = sorted(list(fset1))
    


for r in result:
    print r.strip()

