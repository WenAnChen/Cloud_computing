#!/usr/bin/env python
import sys

month_dict = {
"Mar" : "03"
}

for line in sys.stdin:
        line = line.strip()
        words = line.split()
        time = words[3][1:].split('/')
        day = time[0]
        month = time[1]
        year = time[2][:4]
        hour = time[2][5:7] + ":00:00.000"
        log = "{year}-{month}-{day} T {hour}".format(year=year, month=month_dict[month], day=day, hour=hour)
        print '%s\t%s' % (log, 1)
