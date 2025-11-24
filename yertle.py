# Chapter 4 Turtle Lab
# Jason Jennette
# 02/24/2021
# This program will fill a designated box light brown, and Tiddles will be
# sent to random coordinates until he escapes the box. When escaped he will say
# "Tiddles escaped!" while still inside box will say "Darn!"

import turtle
import random

start = (0, 0)

escaped = False  # Setting flag to false

# Giving turtle his shape and pencolor of square
turtle.shape("turtle")
turtle.pencolor("brown")

# Fillcolor of square
turtle.fillcolor("tan")
turtle.begin_fill()

# Drawing square and fill with color
turtle.penup()
turtle.goto(100, 100)
turtle.pendown()
turtle.goto(-100, 100)
turtle.goto(-100, -100)
turtle.goto(100, -100)
turtle.goto(100, 100)
turtle.end_fill()

turtle.fillcolor("green")

# Returning to (0,0)
turtle.penup()
# turtle.goto(0,0)
turtle.goto(start)
turtle.pendown()

turtle.pencolor("black")  # setting turtles pencolor to black

# WHILE loop sending the turtle to random coordinates.
while not escaped:

    direction = random.randint(0, 359)
    distance = random.randint(1, 200)

    turtle.left(direction)
    turtle.forward(distance)

    # Did the turtle escape out the sides
    if turtle.xcor() > 100 or turtle.xcor() < -100:
        turtle.write("Yertle has escaped!")
        escaped = True

    # Did the turtle escape out the top or bottom
    elif turtle.ycor() > 100 or turtle.ycor() < -100:
        turtle.write("Yertle has escaped!")
        escaped = True

    else:
        turtle.write("Darn!")
        escaped=True

turtle.done()
turtle.bye()