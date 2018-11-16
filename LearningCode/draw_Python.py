import turtle as t
def drawSnake(radius,angle,length):
    mycolor=["black","red","blue","yellow"]
    yocolor=["green","purple","violet","orange"]
    t.seth(-40);
    for i in range(length):
        t.circle(radius,angle)
        t.pencolor(mycolor[i])
        t.circle(-radius,angle)
        t.pencolor(yocolor[i])
    t.seth(0)
    t.fd(40)
    t.circle(16,180)
    t.fd(40)

t.setup(650,350)
t.penup()
t.fd(-250)
t.pendown()
t.pensize(15)
t.pencolor((160,32,240))
drawSnake(40 ,80, 4)
t.done()
