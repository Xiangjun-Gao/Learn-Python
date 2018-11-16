#calculate_pi.py
from random import random,seed
from math import sqrt
from time import sleep,clock
darts=2**24
hits=0.0
clock()
seed(125)
for i in range(1,darts+1):
    x,y=random(),random()
    if(sqrt(x*x+y*y)<=1):
        hits+=1
pi=(hits/darts)*4
print("pi:{}".format(pi))
print("t={}".format(clock()))
