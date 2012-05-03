#! /usr/bin/python

import sys, os

if len(sys.argv) < 3:
    print "Need to pass a directory of features and a file to analyze and a step size"
    print "Example: ./analyzer.py features data.trace 100"
    exit()

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

results = {}
for i, feat in enumerate(features):
    results[feature_files[i]] = []
    for j in range(0, len(data_list), step):
        stop = int(len(feat) * 5 + j)
        if stop > len(data_list):
            stop = len(data_list)
        data_set = set()
        data_set = set(data_list[j: stop])

        res = data_set & feat
        result = float(len(res)) / len(feat)
        results[feature_files[i]].append(result)



# outputs a file readable by gnuplot
for key in results.keys():
    gp = open(key + '.gp', 'w')
    for i, result in enumerate(results[key]):
        line = str(float(i*step)) + " " + str(result) + "\n"
        gp.write(line)

