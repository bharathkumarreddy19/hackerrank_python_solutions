import calendar

import datetime 
mm,dd,yy = map(int, input().split())

print(list(calendar.day_name)[calendar.weekday(yy, mm, dd)].upper())
