import turtle
def draw_multiple_square(t,sz):
    for i in range (4):
        t.forward(sz)
        t.left(90)

wn=turtle.Screen()
wn.bgcolor("lightgreen")

tess=turtle.Turtle()
tess.pensize(3)
tess.color("blue")


size=100
for i in range(20):
    draw_multiple_square(tess,size)
    tess.right(18)
wn.mainloop()