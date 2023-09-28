import turtle
screen= turtle.Screen()
screen.setup(500,500,startx=0,starty=100)
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
t.pencolor("red")
x=0
y=0
t.speed(0)
t.penup()
t.goto(0,200)
t.pendown()
while(True):
    t.forward(x)
    t.right(y)
    x+=3
    y+=1
    if y == 210:
        break
    t.hideturtle()
turtle.done()