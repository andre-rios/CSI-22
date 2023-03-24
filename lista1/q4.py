import turtle
import math

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.pencolor("blue")
alex.color("blue")
alex.width(3)

def draw_squares(t, squares):

    for i in range(4*squares):
        t.forward(i*4)
        t.right(90)

def draw_spiral(t, squares):

    for i in range(4*squares):
        t.forward(i*4)
        t.right(89)

draw_spiral(alex, 25)

wn.mainloop()