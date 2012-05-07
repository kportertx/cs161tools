#! /usr/bin/python

import sys, os

def help():
    print "Need to pass a feature_data directory and a feature destination directory."
    print "Options:\n\t-i\tremove instructions\n\t-dw\tremove data writes\n\t-dr\tremove data reads"
    print "Example: buildFeatures.py -i -dw src/ dest/"
    print "Expected directory stucture\n\tFeatData\n\t\tFeat1\n\t\t\tTarget1\n\t\t\tTarget2\n\t\tFeat2\n\t\t\tTarget1\n\tETC...\n"
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

path = sys.argv[1].strip()
dest = sys.argv[2].strip()

def stripSlash(directory):
    return directory[:-1] if directory[-1] == '/' else directory

path = stripSlash(path)
dest = stripSlash(dest)

if not (os.path.isdir(path) and os.path.isdir(dest)):
    help()

ls = os.listdir(path)
features = filter(os.path.isdir, map(lambda d: path + '/' + d, ls))
feat_sets = []

for feat in features: # set difference all of the features (must be outside this loop)
    print feat
    targets = os.listdir(feat)
    targets = filter(os.path.isdir, map(lambda d: feat + '/' + d, targets))
    if len(targets) == 0:
        features.remove(feat)
        continue

    target_set = None
    for target in targets: # Intersect all of the targets
        print target
        traces = os.listdir(target)
        traces = filter(os.path.isfile, map(lambda f: target + '/' + f, traces))
        if len(traces) == 0:
            targets.remove(target)
            continue

        trace_set = set()
        for trace in traces: # Union all the traces
            f = open(trace, 'r')
            for l in f:
                s = l.strip().lower()
                if (i and s[0] == 'i') or (dw and s[0:2] == 'dw') or (dr and s[0:2] == 'dr'):
                    trace_set.add(l)
            f.close()
        
        if target_set is None:
            target_set = trace_set
        else:
            target_set &= trace_set

    if len(targets) > 0:
        feat_sets.append(target_set)

results = []
for fset1 in feat_sets: # set difference all of the features from each other
    result = fset1.copy()
    for fset2 in feat_sets:
        if not fset1 is fset2:
            result -= fset2
    results.append(result)

for i, result in enumerate(results):
    f = open(dest + '/' + os.path.basename(features[i]) + '.feat', 'w')
    for l in result:
        f.write(l)
    f.close()
