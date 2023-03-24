import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.pencolor("hotpink")
tess.color("hotpink")
tess.width(4)

def draw_poly(t, n, sz):

    for i in range(n):
        t.forward(sz)
        t.left(360/n)

draw_poly(tess,15,50)

wn.mainloop()