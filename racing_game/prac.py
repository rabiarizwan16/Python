import turtle


#Create start button
start_button = turtle.Turtle()
start_button.shape("square")
start_button.color("green")
start_button.penup()
start_button.goto(-100, 250)
start_button.write("Start", align="center", font=("Arial", 16, "normal"))

# Create stop button
stop_button = turtle.Turtle()
stop_button.shape("square")
stop_button.color("red")
stop_button.penup()
stop_button.goto(100, 250)
stop_button.write("Stop", align="center", font=("Arial", 16, "normal"))

# Global variable to control game state
game_running = False

# Function to start the game
def start_game(x, y):
    global game_running
    game_running = True
    player.sety(-250)
    while game_running:
        player.forward(1)
        if player.ycor() > 250:
            player.goto(0, -250)
        screen.update()

# Function to stop the game
def stop_game(x, y):
    global game_running
    game_running = False

# Bind the buttons to the functions
start_button.onclick(start_game)
stop_button.onclick(stop_game)

# Keep the window open
turtle.done()
