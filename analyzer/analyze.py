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
remove = []

for f in feature_files:
    file_path = feature_path + "/" + f
    if not os.path.isfile(file_path):
        remove.append(f)

for f in remove:
    feature_files.remove(f)

for f in feature_files:
    file_path = feature_path + "/" + f
    file_handle = open(file_path, 'r')
    feature = set(file_handle.readlines())
    file_handle.close()
    features.append(feature)

data = sys.argv[2]
file_handle = open(data, 'r')
data_list = file_handle.readlines()
step = int(sys.argv[3])
tstep = step

def processFeature(jfeat):
    j, feat = jfeat
    stop = j + tstep 
    if stop > len(data_list):
        stop = len(data_list)
    data_set = set(data_list[j: stop])
    
    res = data_set & feat
    return float(len(res)) / (stop - j)

num_features = len(features)
denom = len(features)
data_len = len(data_list)

p = multiprocessing.Pool(num_processes)
percent_complete = 0
sys.stdout.write("\r%d%%" %percent_complete)
sys.stdout.flush()

for z, feat in enumerate(features):
    gp = open(feature_files[z] + '.gp', 'w')
    tstep = min(step, len(feat))  # if step size is < len(feat) then overized step with length of feature
    data = p.map(processFeature, map(lambda j: (j, feat), range(0, data_len, tstep)))
    for i, result in enumerate(data):
        # outputs a file readable by gnuplot
<<<<<<< HEAD
        if result > 0.3:
=======
        if result != 0.0:  # do not print 0.0.  This just reduces number of points and make gunplot work a little better
>>>>>>> 1bd188b5d8959ee791ad32aa47096fa237d01b80
            line = str(float(i*step)) + " " + str(result) + "\n"
            gp.write(line)
    gp.close()

    percent_complete = int(100 * (float(z+1)/float(denom)))
    sys.stdout.write("\r%d%%" %percent_complete)
    sys.stdout.flush()

result = []

print "\ndone"
