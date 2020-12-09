#!/usr/bin/env python
import sys

for line in sys.stdin:
	line = line.strip()
	if len(line) <= 1 or 'C/A' in line:
		continue

	data = line.split(',')
		
	scp = data[2]
	station = data[3]
	date = data[6]
	time = data[7]
	entries = int(data[9])
	exits = int(data[10])

	datedetail = date.split('/')
	timedetail = time.split(':')
	hour = timedetail[0]
	month = datedetail[0]
	year = datedetail[2]
	if hour == '00' or hour == '01' or hour == '02' or hour == '03':
		if year == '2020':
			print '%s,%s,%s,%s,%s' % (station, date, scp, entries, exits)