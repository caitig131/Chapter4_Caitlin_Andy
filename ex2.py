import turtle
def draw_multiple_square(t,sz):
    for i in range (4):
        t.forward(sz)
        t.left(90)

wn=turtle.Screen()
wn.bgcolor("lightgreen")

tess=turtle.Turtle()
tess.pensize(3)
tess.color("hotpink")


size=20
for i in range(5):
    draw_multiple_square(tess,size)
    tess.penup()
    tess.right(90)
    tess.forward(10)
    tess.right(90)
    tess.forward(10)
    tess.right(180)
    size=size+20
    tess.pendown()
    
wn.mainloop()
    
