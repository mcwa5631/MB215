import turtle
import tkinter.simpledialog as simpledialog

window = turtle.Screen()
window.title("Turtle Graphics Example")
window.bgcolor("white")
my_turtle = turtle.Turtle()
my_turtle.pensize(3)
my_turtle.color("blue")
my_turtle.forward(100)
my_turtle.right(90)
my_turtle.forward(50)
my_turtle.left(90)
my_turtle.penup()
my_turtle.goto(50, 50)
my_turtle.pendown()
my_turtle.circle(25)
my_turtle.dot(10)
my_turtle.setheading(0)
my_turtle.color("red")
my_turtle.begin_fill()
for _ in range(4):  
    my_turtle.forward(50)
    my_turtle.right(90)
my_turtle.end_fill()
my_turtle.clear()
my_turtle.reset()
my_turtle.hideturtle()
my_turtle.showturtle()



