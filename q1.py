import turtle
import math

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.pencolor("hotpink")
alex.color("hotpink")
alex.width(4)

def draw_square(t, sz):

    for i in range(4):
        t.forward(sz)
        t.left(90)

    t.penup()
    t.right(135)
    t.forward(10*math.sqrt(2))
    t.left(135)
    t.pendown()

for i in range(1,6):
    draw_square(alex, 20*i)

wn.mainloop()