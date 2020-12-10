#!/usr/bin/env python
import sys

for line in sys.stdin:
	line = line.strip()
	if len(line) <= 1 or 'Station' in line:
		continue
	
	data = line.split(',')
	
	station = data[0]
	date = data[1]
	entry = int(data[2])
	exit = int(data[3])

	datedetail = date.strip().split('/')
	month = datedetail[0]

	if entry > 0 and entry < 100000 and exit > 0 and exit < 100000:
		print '%s,%s,%d,%d' % (station, month, entry, exit)
