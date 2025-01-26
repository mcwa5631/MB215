# Import Turtle graphics library
import turtle

# Set up your drawing parameters
ITERATIONS = 40  # Number of times to repeat the pattern
ANGLE = 25       # Angle to turn after each shape is drawn
SIZE = 50      # Size parameter for the shapes

# Set up the Turtle screen and turtle
screen = turtle.Screen()
screen.bgcolor("black")  # Set background color to black for better visibility

pattern_turtle = turtle.Turtle()
pattern_turtle.speed(0)  #Sets speed of drawing
colors = ["blue", "green"]  #Changes between colours blue and green

# Loop to draw the pattern
for i in range(ITERATIONS):
    pattern_turtle.color(colors[i % len(colors)])

#continously draws going forward based on size set earlier, turns right 90 degrees, then left 45 degrees
    for _ in range(4):
        pattern_turtle.forward(SIZE)
        pattern_turtle.right(90)  # Right angle for a square
        pattern_turtle.left(45)

    # Rotate the turtle to prepare for the next shape
    pattern_turtle.right(ANGLE)

# Complete the program with a command to keep the window open
turtle.done()
