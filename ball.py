from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.setposition(0, 0)
        self.ball_speed = 0.1
        self.x_direction = 10
        self.y_direction = 10
        self.penup()

    def move(self):
        new_x = self.xcor() + self.x_direction
        new_y = self.ycor() + self.y_direction
        self.goto(new_x, new_y)

    def bounce(self, axis):
        if axis == "y":
            self.y_direction *= -1
        elif axis == "x":
            self.x_direction *= -1
            self.ball_speed *= 0.9

    def restart(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.x_direction *= -1
