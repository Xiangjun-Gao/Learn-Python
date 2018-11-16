#进度条.py
from time import *
scale=50
print("\n"+"begin".center(scale//2,"-"))
t=clock()

for i in range(scale+1):
    c=(i/scale)*100
    a,b="**"*i,".."*(scale-i)
    t=clock()-t
    print("\r{:<3.0f}%[{}->{}]  {:.2f}s".format(c,a,b,t),end="")
    sleep(0.1)

print("\n"+"end".center(scale//2,"-"))
