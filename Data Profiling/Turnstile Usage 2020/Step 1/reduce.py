#!/usr/bin/env python
import sys

Prev_Station = None
Prev_Date = None
Prev_SCP = None
Station = None
Date = None
SCP = None
total_entry = 0
total_exit = 0 

for line in sys.stdin:
	line = line.strip().split(',')
	Station = line[0]
	Date = line[1]
	SCP = line[2]
	entry = int(line[3])
	exit = int(line[4])
	
	if Prev_Station == Station and Prev_Date == Date:
		if Prev_SCP != SCP:
			Prev_SCP = SCP
			total_entry += entry
			total_exit += exit
	else:
		if Prev_Station is not None:
			print '%s,%s,%d,%d' % (Prev_Station,Prev_Date,total_entry,total_exit)
		Prev_Station = Station
		Prev_Date = Date
		Prev_SCP = SCP
		total_entry = entry
		total_exit = exit
		
if Prev_Station == Station:
	print '%s,%s,%d,%d' % (Prev_Station,Prev_Date,total_entry,total_exit)