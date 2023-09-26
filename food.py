from turtle import Turtle
import random

# Create a class for the food object
class Food(Turtle):

    # Initialize the food object
    def __init__(self):
        super().__init__()  # Call the parent class constructor
        
        # Set the shape, color, and size of the food
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        
        # Position the food randomly
        self.refresh()

    # Method to move the food to a random position
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

# This code defines a Food class for creating food items in a game and explains the key steps.
