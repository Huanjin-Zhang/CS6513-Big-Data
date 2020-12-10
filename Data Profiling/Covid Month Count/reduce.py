#!/usr/bin/env python
import sys

Prev_Month = None
Month = None
Case_total = 0
Hospitalized_total = 0
Death_total = 0

title_month = 'MONTH_OF_INTERSET'
title_case = 'CASE_COUNT'
title_hospitalized = 'HOSPITALIZED_COUNT'
title_death = 'DEATH_COUNT'

print '%s,%s,%s,%s' % (title_month, title_case, title_hospitalized, title_death)

for line in sys.stdin:
	line = line.strip().split(',')
	Month = line[0]
	case_count = int(line[1])
	hospitalized_count = int(line[2])
	death_count = int(line[3])

	if Prev_Month == Month:
		Case_total += case_count
		Hospitalized_total += hospitalized_count
		Death_total += death_count
	
	else:
		if Prev_Month is not None:
			print '%s,%d,%d,%d' % (Prev_Month, Case_total, Hospitalized_total, Death_total)
		Prev_Month = Month
		Case_total = case_count
		Hospitalized_total = hospitalized_count
		Death_total = death_count

if Prev_Month == Month:
	print '%s,%d,%d,%d' % (Prev_Month, Case_total, Hospitalized_total, Death_total)
