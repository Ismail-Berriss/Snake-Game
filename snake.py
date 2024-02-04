from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snack_body = []
        self.create_snake()
        self.head = self.snack_body[0]

    def create_snake(self):
        for i in range(3):
            self.add_portion(i)

    def add_portion(self, position):
        body_portion = Turtle("square")
        body_portion.color("white")
        body_portion.penup()
        body_portion.teleport(x=-MOVE_DISTANCE * position, y=0)
        self.snack_body.append(body_portion)

    def extend(self):
        """Add a new portion to the snake body"""
        self.add_portion(len(self.snack_body))

    def move(self):
        for i in range(len(self.snack_body) - 1, 0, -1):
            new_x = self.snack_body[i - 1].xcor()
            new_y = self.snack_body[i - 1].ycor()
            self.snack_body[i].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

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
