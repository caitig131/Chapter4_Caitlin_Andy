import turtle
def draw_star(t,sz):
    for i in range(5):
        t.forward(100) 
        t.right(144)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess=turtle.Turtle()
tess.pensize(3)
tess.color("hotpink")
 

size=(7)
for i in range (5):
    draw_star(tess,size)
    tess.penup()
    tess.forward(350)
    tess.right(144)
    tess.pendown()
    
               
wn.mainloop()