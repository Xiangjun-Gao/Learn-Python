#DrawSevenSegDisplay.py
import turtle,datetime
def drawLine(draw):#绘制单段数码管
    if draw :
        turtle.penup()
        turtle.fd(5)
        turtle.pendown()
        turtle.fd(30)
        turtle.penup()
        turtle.fd(5)
    else :
        turtle.fd(40)
    turtle.right(90)

def drawDigit(d):#根据数字绘制七段数码管
    drawLine(True) if d in [2,3,4,5,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
    
def drawDate(date):#获得想要输入的数字
    for i in date:
        
        if i=='-':
            turtle.write('年',font=("Arial",18,"normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i=='=':
            turtle.write('月',font=("Arial",18,"normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        elif i=='+':
            turtle.write('日',font=("Arial",18,"normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        else:
            drawDigit(eval(i))

def main():
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    turtle.pencolor("violet")
    date=datetime.datetime.now().strftime("%Y-%m=%d+")
    drawDate(date)
    turtle.hideturtle()
main()
