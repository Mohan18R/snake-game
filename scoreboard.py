# Import the Turtle module
from turtle import Turtle

# Define constants for alignment and font style
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

# Create a Scoreboard class that inherits from Turtle
class Scoreboard(Turtle):

    # Constructor method to initialize the scoreboard
    def __init__(self):
        super().__init__()  # Call the parent class constructor
        
        # Initialize the score to 0
        self.score = 0
        
        # Set the text color to white
        self.color("white")
        
        # Lift the pen to prevent drawing while positioning
        self.penup()
        
        # Position the scoreboard at the top center of the screen
        self.goto(0, 270)
        
        # Hide the turtle icon
        self.hideturtle()
        
        # Update the scoreboard with the initial score
        self.update_scoreboard()

    # Method to update the scoreboard with the current score
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    # Method to display "GAME OVER" when the game ends
    def game_over(self):
        self.goto(0, 0)  # Position the text at the center of the screen
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    # Method to increase the score by 1
    def increase_score(self):
        self.score += 1  # Increment the score by 1
        self.clear()  # Clear the previous score
        self.update_scoreboard()  # Update the scoreboard with the new score

# This code defines a Scoreboard class for displaying and updating the game's score and provides comments to explain its functionality.
