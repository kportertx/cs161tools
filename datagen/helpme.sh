#!/bin/bash

count=20

while read -r line
  do
    touch traces/trace$count.txt
    echo "QUERY => $line" >> traces/trace$count.txt
    count=$((count+1))
  done < select_qry_list_rem
