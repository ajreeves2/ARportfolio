#Anyla Reeves
#9/24/24
#period:5

#init
import turtle
anyla = turtle.Turtle()
#Functions
def starfish(color):
    anyla.color(color)
    anyla.pensize(5)
    #Draw a single element on the screen
#executing loop 5 timnes for a star
    anyla.begin_fill()
    for i in range(5):
        

        #moving turtle 100 units forward
        anyla.forward(100)

        #rotating turtle 144 degree right
        anyla.right(144)
      
    anyla.end_fill()
def all_starfish():
    starfish("black")
    anyla.penup()
    anyla.goto(-60, 90)
    anyla.pendown()
    starfish("#ff0066")
    anyla.penup()
    anyla.goto(90, -60)
    anyla.pendown()
    starfish("green")
    anyla.penup()
    anyla.goto(100, 90)
    anyla.pendown()
    starfish("blue")
    anyla.penup()
    anyla.goto(-200, 60)
    anyla.pendown()
    starfish("pink")
    anyla.penup()
    anyla.goto(-300, 100)
    anyla.pendown()
    starfish("purple")
    anyla.penup()
    anyla.goto(300,-90)
    anyla.pendown()
    starfish("orange")
    anyla.penup()
    anyla.goto(-300,10)
    anyla.pendown()
    starfish("#cc0066")
    anyla.penup()
    anyla.goto(-400, -100)
    anyla.pendown()
    starfish("brown")
    anyla.penup()
    anyla.goto(250, -10)
    anyla.pendown
    starfish("red")
    anyla.penup()
    anyla.goto(-100, -30)
    anyla.pendown()
    starfish("grey")
    anyla.penup()
    anyla.goto(-200, -90)
    anyla.pendown()
    starfish("yellow")
   
#Main
all_starfish()




