from turtle import *
import time
screen = Screen()
screen.bgcolor("wheat")
turtle = Turtle()
turtle.pencolor("green")
def drawValue():
    length = 100
    turtle.forward(length)
    turtle.backward(length)
    turtle.right(30)
        
for x in range(1, 12 + 1):
    drawValue();

def drawValue2():
    length = 40
    turtle.forward(length)
    turtle.right(length)
    turtle.backward(length)
    turtle.left(10)
    

for j in range(1, 12 + 1):
    drawValue2();
    
turtle.backward(40)

def drawValue3():
    length = 40
    turtle.backward(length)
    turtle.left(length)
    turtle.forward(length)
    turtle.right(10)
    

for i in range(1, 13 + 1):
    drawValue3()
    
time.sleep(10)