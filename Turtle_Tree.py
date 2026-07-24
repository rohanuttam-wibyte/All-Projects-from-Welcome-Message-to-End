import turtle
import math

t = turtle.Turtle()
# Turns off the turtle animation so it draws the entire frame instantly
turtle.tracer(0) 
turtle.bgcolor("white")
t.hideturtle() # Hides the turtle cursor for cleaner visuals

def branch(sz, level, time_val):
    if level < 3:
        t.color("forestgreen")
    else:
        t.color("saddlebrown")
        
    t.pensize(level)

    if level > 0:
        t.forward(sz)
        
        # Calculate a slight sway angle using a sine wave
        # The sine wave naturally oscillates back and forth
        sway = math.sin(time_val) * 6 
        
        # Right branch (adds the sway)
        t.right(30 + sway)
        branch(0.8 * sz, level - 1, time_val)
        
        # Left branch 
        t.left(60) 
        branch(0.8 * sz, level - 1, time_val)
        
        # Return to the original heading (subtracts the sway to balance)
        t.right(30 - sway)
        
        if level < 3:
            t.color("forestgreen")
        else:
            t.color("saddlebrown")
            
        t.penup()
        t.backward(sz)
        t.pendown()

# Animation loop
time_val = 0

while True:
    t.clear() # Clear the previous frame
    
    # Reset starting position and angle for the new frame
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.setheading(90)
    
    # Draw the tree for the current "time"
    branch(80, 10, time_val)
    
    # Update the screen all at once
    turtle.update()
    
    # Advance the time variable to move the wave forward
    time_val += 0.1
