#!/usr/bin/env python
import sys

for line in sys.stdin:
	line = line.strip()
	if len(line) <= 1:
		continue
	
	data = line.split(',')
	station = data[0]
	date = data[1]
	entry = int(data[2])
	exit = int(data[3])
	
	print '%s,%s,%d,%d' % (station,date,entry,exit)