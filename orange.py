#Anyla Reeves
#9/13/2024
#Period:5

#Init
import turtle
anyla = turtle.Turtle()
anyla.color("orange")
anyla.pensize(10)
#Function

def orange():
    anyla.left(90)
    anyla.circle(-250, 450)
    anyla.right(100)
    anyla.left(50)
    anyla.right(130)
    for i in range (3):
        anyla.color("green")
        anyla.forward(90)
        anyla.right(120)   

#main
orange()

import turtle

#create a turtle object
anyla = turtle.Turtle ()

#set the color of the stem
anyla.color ("brown")

#draw the stem
anyla.penup()
anyla.goto(250, 250) #start position of the stem
anyla.pendown()
anyla.setheading(90) #Point the turtle upwards
anyla.width(10) #set the width of the stem
anyla.forward(150) #draw the stem

#draw the eyes
anyla.penup()
anyla.goto(150, 100)
anyla.pendown()
anyla.begin_fill()
anyla.color("black")
anyla.circle(15)
anyla.end_fill()

#draw the eyes
anyla.penup()
anyla.goto(250, 100)
anyla.pendown()
anyla.begin_fill()
anyla.color("black")
anyla.circle(15)
anyla.end_fill()

#draw the smile
anyla.penup()
anyla.goto(80, -15)
anyla.pendown()
anyla.setheading(300)
anyla.circle(150,125)

#main
stem()
