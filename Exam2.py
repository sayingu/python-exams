import turtle

t = turtle.Turtle()
t.ht()

def drawRectangle(size):
    global t

    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)

def prepareNextRectangle():
    t.penup()
    t.left(180)
    t.forward(10)
    t.right(90)
    t.forward(10)
    t.pendown()

drawRectangle(100)
prepareNextRectangle()
drawRectangle(80)
prepareNextRectangle()
drawRectangle(60)

turtle.exitonclick()
