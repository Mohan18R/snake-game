# Import the Turtle module
from turtle import Turtle

# Define constants for starting positions, move distance, and directions
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# Create a Snake class
class Snake:

    # Constructor method to initialize the snake
    def __init__(self):
        self.segments = []  # List to store snake segments
        self.create_snake()  # Create the initial snake
        self.head = self.segments[0]  # The snake's head

    # Method to create the initial snake with three segments
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    # Method to add a new segment to the snake
    def add_segment(self, position):
        new_segment = Turtle("square")  # Create a new snake segment
        new_segment.color("white")  # Set the color of the segment
        new_segment.penup()  # Lift the pen to prevent drawing
        new_segment.goto(position)  # Move the segment to the given position
        self.segments.append(new_segment)  # Add the segment to the snake's segments list

    # Method to extend the snake by adding a new segment at the end
    def extend(self):
        self.add_segment(self.segments[-1].position())

    # Method to move the snake forward
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Methods to change the snake's direction
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

# This code defines a Snake class for creating and controlling a snake in the game and provides comments to explain its functionality.
