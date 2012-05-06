#! /usr/bin/python

import sys, os

def help():
    print "Options:\n\t-i\tremove instructions\n\t-dw\tremove data writes\n\t-dr\tremove data reads"
    print "Example: ./remove.py -i -dw source dest"
    exit()
    
if len(sys.argv) < 3:
    help()

i = True
dw = True
dr = True

while len(sys.argv) > 3:
    opt = sys.argv.pop(1).strip().lower()

    if opt == '-i':
        i = False
    elif opt == '-dw':
        dw = False
    elif opt == '-dr':
        dr = False
    else:
        print "Error: Invalid option: ", opt
        help()


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
            if (i and s[0] == 'i') or (dw and s[0:2] == 'dw') or (dr and s[0:2] == 'dr'):
                dest_handle.write(l)


