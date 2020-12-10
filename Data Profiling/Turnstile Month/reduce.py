#!/usr/bin/env python
import sys

Prev_Station = None
Prev_Month = None

month_entry = 0
month_exit = 0

title_station = 'Station'
title_month = 'Month'
title_entry = 'Entries Month'
title_exit = 'Exits Month'

print '%s,%s,%s,%s' % (title_station, title_month, title_entry, title_exit)

for line in sys.stdin:
	line = line.strip().split(',')
	Station = line[0]
	Month = line[1]
	daily_entry = int(line[2])
	daily_exit = int(line[3])

	if Prev_Month == Month:
		month_entry += daily_entry
		month_exit += daily_exit
	
	else:
		if Prev_Month is not None:
			print '%s,%s,%d,%d' % (Prev_Station, Prev_Month, month_entry, month_exit)
		Prev_Station = Station
		Prev_Month = Month
		month_entry = daily_entry
		month_exit = daily_exit

if Prev_Month == Month:
	print '%s,%s,%d,%d' % (Prev_Station, Prev_Month, month_entry, month_exit)		
