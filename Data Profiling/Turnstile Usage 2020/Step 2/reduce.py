#!/usr/bin/env python
import sys

Prev_Station = None
Station = None
Prev_Date = None
Date = None
Prev_Entry = None
Prev_Exit = None

print 'Station,Date,Daily_Entry,Daily_Exit'

for line in sys.stdin:
	line = line.strip().split(',')
	Station = line[0]
	Date = line[1]
	entry_sum = int(line[2])
	exit_sum = int(line[3])

	if Prev_Station is not None:
                if Prev_Station == Station:
                        entry = entry_sum - Prev_Entry
                        exit = exit_sum - Prev_Exit
                        print '%s,%s,%d,%d' % (Prev_Station,Prev_Date,entry,exit)

        Prev_Station = Station
        Prev_Date = Date
        Prev_Entry = entry_sum
        Prev_Exit = exit_sum