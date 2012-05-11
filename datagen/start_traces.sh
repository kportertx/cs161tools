#!/bin/bash

count=0

while read -r line
  do
    sync
    sync
    sync
    starts=`wc -l log.txt`
    sync
    sync
    sync
    sleep 5
    #python worker.py "$line"
    mysql -u root --password="madhacker" npages -e "$line" > /dev/null
    sync
    sync
    sync
    sleep 5
    sync
    sync
    sync
    touch traces/trace$count.txt
    echo "Query => $line" >> traces/trace$count.txt
    end=`wc -l log.txt`
    echo "Start $starts , End $end" >> traces/trace$count.txt
    sync
    sync
    sync
    sleep 5
    count=$((count+1))
  done < select_qry_list
