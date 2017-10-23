import turtle
wn=turtle.Screen()
def draw_equitriangle(t,sz):
    for i in range (3):
        t.forward(150)
        t.left(120)

tess=turtle.Turtle()
tess.pensize(3)

size=7
for i in range(1):
    draw_equitriangle(tess,size)
    
wn.mainloop()