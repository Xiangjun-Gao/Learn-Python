import turtle as t
   
def tree(branchLen):  
    if branchLen>5:  
        t.forward(branchLen)  
        t.right(30)
        tree(branchLen-10)  
        t.left(60)  
        tree(branchLen-10)  
        t.right(30)  
        t.backward(branchLen)  
   
def main():   
    t.left(90)  
    t.penup()  
    t.backward(100)  
    t.pendown()  
    t.color("green")
    t.pensize(5)
    t.speed(500)
    tree(75)  
    hideturtle()  
   
main()  
