#! /usr/bin/python

import sys, os, multiprocessing

if len(sys.argv) < 3:
    print "Need to pass a directory of features and a file to analyze and a step size"
    print "Example: ./analyzer.py features data.trace 100"
    exit()

cpu_count = multiprocessing.cpu_count()
num_processes = cpu_count + 2

feature_path = sys.argv[1]
feature_files = os.listdir(feature_path)
features = []

for f in feature_files:
    file_path = feature_path + "/" + f
    if os.path.isfile(file_path):
        feature = set()
        file_handle = open(file_path, 'r')
        for l in file_handle:
            feature.add(l)
        features.append(feature)

data = sys.argv[2]
file_handle = open(data, 'r')
data_list = file_handle.readlines()
step = int(sys.argv[3])

def processFeature(jfeat):
    j, feat = jfeat
    stop = int(len(feat) * 5 + j)
    if stop > len(data_list):
        stop = len(data_list)
    data_set = set()
    data_set = set(data_list[j: stop])
    
    res = data_set & feat
    return float(len(res)) / len(feat)

num_features = len(features)
denom = len(features)
data_len = len(data_list)

p = multiprocessing.Pool(num_processes)
percent_complete = int(100 * (float(z+1)/float(denom)))
sys.stdout.write("\r%d%%" %percent_complete)
sys.stdout.flush()
for z, feat in enumerate(features):
    gp = open(feature_files[z] + '.gp', 'w')
    for i, result in enumerate(p.map(processFeature, map(lambda j: (j, feat), range(0, data_len, step)))):
        # outputs a file readable by gnuplot
        line = str(float(i*step)) + " " + str(result) + "\n"
        gp.write(line)
    gp.close()

    percent_complete = int(100 * (float(z+1)/float(denom)))
    sys.stdout.write("\r%d%%" %percent_complete)
    sys.stdout.flush()

