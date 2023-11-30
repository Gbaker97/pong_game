from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.penup()
        self.setposition(pos)

    def up(self):
        updated_y = self.ycor() + 20
        self.goto(self.xcor(), updated_y)

    def down(self):
        updated_y = self.ycor() - 20
        self.goto(self.xcor(), updated_y)
