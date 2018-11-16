#DayDayup365.py
from turtle import *
def dayup(n):
    dayup=1.0
    for i in range(365):
        if i%7 in[0,6]:
            dayup+=n
        else:
            dayup=dayup
    return dayup
a=[0.001, 0.002, 0.003, 0.004, 0.005 ,0.006, 0.007, 0.008 ,0.009 ,0.010]
for i in range(10):
    print("{:.2f}".format( dayup(a[i])))
    #print("{:.2f}".format(i))
    
