#!/bin/bash

/home/cs161/CachegrindMemMod/vg-in-place --tool=cachegrind --trace-children=yes /usr/sbin/mysqld 2>log.txt


