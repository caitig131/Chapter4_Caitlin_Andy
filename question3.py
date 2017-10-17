import turtle
wn = turtle.Screen()
wn.bgcolor("lightpink")
caitlin = turtle.Turtle()
caitlin.color("magenta")
caitlin.pensize(3)
def draw_poly(turt,num,size):
    for i in range(num):
        turt.forward(size)
        turt.left(360/num)
        
draw_poly(caitlin,8,50)