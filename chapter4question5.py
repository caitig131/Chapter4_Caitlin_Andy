import turtle

myPen = turtle.Turtle()
myPen.speed(0)


side=400
myPen.penup()
myPen.goto(-200,-200) 
myPen.pendown()


for i in range (1,100):
   myPen.forward(side)
   myPen.left(90)
   side=side-4
