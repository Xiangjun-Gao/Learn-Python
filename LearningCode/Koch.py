#DrawKoch.py
from turtle import *

def koch(size,n):
    if n==0:
        fd(size)
    else:
        for i in [0,60,-120,60]:
            left(i)
            koch(size/3,n-1)
            
def main():
    n=eval(input("n="))
    size=eval(input("size="))
    setup(800,350)
    penup()
    pencolor("blue")
    speed(100)
    goto(-300,100)
    pendown()
    pensize(2)
    koch(size,n)
    right(120)
    koch(size,n)
    right(120)
    koch(size,n)
    hideturtle()
main()


    
