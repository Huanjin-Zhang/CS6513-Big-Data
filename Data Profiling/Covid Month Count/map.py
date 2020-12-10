#!/usr/bin/env python
import sys

for line in sys.stdin:
	lie = line.strip()
	if len(line) <= 1 or 'DATE_OF_INTEREST' in line:
		continue

	data = line.split(',')
	
	date = data[0]
	case_count = int(data[1])
	hospitalized_count = int(data[2])
	death_count = int(data[3])

	#get month
	datedetail = date.split('/')
	month = datedetail[0]

	if month != '02':
		print '%s,%d,%d,%d' % (month, case_count, hospitalized_count, death_count)
