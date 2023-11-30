from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.left_score = 0
        self.right_score = 0
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=("Bauhaus 93", 80, "normal"))
        self.goto(100, 200)
        self.write(self.left_score, align="center", font=("Bauhaus 93", 80, "normal"))

    def update_score(self, player):
        if player == "l":
            self.left_score += 1
        if player == "r":
            self.right_score += 1
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=("Bauhaus 93", 80, "normal"))
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=("Bauhaus 93", 80, "normal"))

    def end_game(self):
        if self.left_score == 10:
            self.goto(0, 0)
            self.color("lime")
            self.write("LEFT PLAYER WON.", align="center", font=("Bauhaus 93", 80, "bold"))
            return False
        if self.right_score == 10:
            self.goto(0, 0)
            self.color("lime")
            self.write("RIGHT PLAYER WON.", align="center", font=("Bauhaus 93", 60, "bold"))
            return False
        else:
            return True
