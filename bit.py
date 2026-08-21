import turtle
import time

t = turtle.Turtle()
ts = turtle.Screen()
ts.bgcolor("darkgreen") 
ts.tracer(0)
t.speed(0)
t.hideturtle()
t.color("white") 

def draw_player_zone(x, y, has_ball):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    
    # Draw the player's patch of grass
    t.fillcolor("forestgreen")
    t.begin_fill()
    for _ in range(4):
        t.forward(20)
        t.left(90)
    t.end_fill()
    t.penup()
    
    # If the bit is 1, draw a "soccer ball"
    if has_ball == 1:
        t.goto(x + 10, y + 2) 
        t.fillcolor("white")
        t.begin_fill()
        t.circle(8) 
        t.end_fill()
        
        # Add a black outline to the ball
        t.color("black")
        t.pendown()
        t.circle(8) 
        t.penup()
        t.color("white") 

# Coordinates for a full 11-player 4-3-3 Formation
positions = [
    (0, -140),    # GK
    (-120, -70),  # LB
    (-40, -70),   # LCB
    (40, -70),    # RCB
    (120, -70),   # RB
    (-80, 0),     # LCM
    (0, 0),       # CM
    (80, 0),      # RCM
    (-80, 70),    # LW
    (0, 70),      # ST
    (80, 70)      # RW
]

# Position names to display above each player
player_names = [
    "GK", 
    "LB", 
    "LCB", 
    "RCB", 
    "RB", 
    "LCM", 
    "CM", 
    "RCM", 
    "LW", 
    "ST", 
    "RW"
]

# Start with the ball at the Goalkeeper
pattern = 0b00000000001 
direction = "forward" 

for cnt in range(1000):
    
    if direction == "forward":
        pattern = pattern << 1 # Pass up the field
        if pattern >= 0b10000000000: # If ball reaches the last player (RW)
            direction = "backward"   
            
    elif direction == "backward":
        pattern = pattern >> 1 # Pass back down the field
        if pattern <= 0b00000000001: # If ball reaches Goalkeeper (GK)
            direction = "forward"    
            
    t.clear() 
    
    # --- NEW: Draw the Main Title ---
    t.goto(0, 195)
    t.write("⚽ Pitch Perfect Passing ⚽", align="center", font=("Arial", 16, "bold"))
    
    # Draw the Position Key
    t.goto(0, 165)
    t.write("POSITION KEY", align="center", font=("Arial", 10, "bold", "underline"))
    t.goto(0, 145)
    t.write("GK: Goalkeeper  |  LB/RB: Left/Right Back  |  LCB/RCB: Left/Right Center Back", align="center", font=("Arial", 9, "normal"))
    t.goto(0, 130)
    t.write("LCM/CM/RCM: Midfielders  |  LW/RW: Left/Right Wing  |  ST: Striker", align="center", font=("Arial", 9, "normal"))
    
    # Check all 11 players to draw the ball
    for kk in range(11):
        b = (pattern & (2**kk)) >> kk
        
        x_pos, y_pos = positions[kk]
        
        # Write the actual Position Name
        t.goto(x_pos, y_pos + 25)
        t.write(player_names[kk], align="center", font=("Arial", 12, "bold"))
        
        # Draw the grass and the ball
        draw_player_zone(x_pos - 10, y_pos - 10, b)
        
    ts.update()
    time.sleep(0.4)
