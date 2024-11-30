"""
modules is a way to reuse a code written
by someone else
"""
"""
fndng square root usng free modeluse
eg math modules
"""
import math

sqr=math.sqrt(16)
print(sqr)
"""
fndng math modules/functions
"""
mmodules=dir(math)
print(mmodules)

x=math.log10(1000)
print(x)

v=math.floor(2.3)
c=math.ceil(2.3)
print(v)
print(c)

"""
Dealing with calender module
"""
import  calendar

cal = calendar.month(1997,10)
print(cal)

"""
checking if there year is a leap year or not
"""
print(calendar.isleap(1997))
print(calendar.isleap(2016))
print(dir(calendar))

"""
Writing your own module
"""