import numpy as np
import random
import turtle as t
a=np.array( [-0.64,0;0,0.5;0.86,0.25],
            [-0.04,-0.47;0.07,-0.02;0.49,0.51],  
            [0.2,0.33;-0.49,0.43;0.44,0.25],  
            [0.46,-0.25;0.41,0.36;0.25,0.57],  
            [-0.06,0.45;-0.07,-0.11;0.59,0.1]）
x0=np.array(0,0)
p0=np.array(0.06,0.22,0.23,0.24,0.25);

def fenxing(x0):
    for i in range(1000):
        p=random.random()
        if p<np.add.reduce(p0(:1)):
            x0=x0*a[0][:2]+a[0][2]
            
        elif p<np.add.reduce(p0(:2)):
            x0=x0*a[1][:2]+a[1][2]
            
        elif p<np.add.reduce(p0(:3)):
            x0=x0*a[2][:2]+a[2][2]
            
        elif p<np.add.reduce(p0(:4)):
            x0=x0*a[3][:2]+a[3][2]

        else:
            x0=x0*a[3][:2]+a[3][2]
        t.goto(x0[0],x0[1])
        t.pendown()
        t.goto(x0[0],x0[1])
        t.penup()
            
def main():
        t.setup(650,300)
        t.pensize(2)
        t.pencolor("green")
        fenxing(x0)
        
