#!/bin/bash

/home/cs161/CachegrindMemMod/vg-in-place --tool=cachegrind --I1=32768,2,64 --D1=32768,2,64 --LL=131072,2,64 --trace-children=yes /usr/sbin/mysqld 2>log.txt


