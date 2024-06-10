from time_calculator import *

a = add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

b = add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

c = add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

d = add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

e = add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

f = add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)