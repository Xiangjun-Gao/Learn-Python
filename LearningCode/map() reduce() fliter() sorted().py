#map() reduce() fliter() sorted()
list(map(str,range(5)))

def add5(v):
    return v+5
list(map(add5,range(10))) #map函数返回一个惰性序列，需要用list函数让其显示表达

from functools import reduce
def add(x,y):
    return x+y
reduce(add,list(map(str,range(5)))) #add函数可以用lambda函数替换
    
def isodd(x):
    d={1:False,0:True}
    return d[x%2]

seq=[1,2,3,4,5,6,7,8,9]
filter(isodd,seq)#filter函数返回一个惰性序列，需要用list函数让其显示表达

ls=["Lebron","kobe","jordan","Duncan","O'neal"]
print(sorted(ls,key=str.lower,reverse=True))
