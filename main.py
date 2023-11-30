import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.title("Pong")
screen.screensize(800, 600)
screen.listen()


def start_game():
    screen.clear()
    screen.bgcolor("black")
    screen.tracer(0)

    r_paddle = Paddle((350, 0))
    l_paddle = Paddle((-350, 0))

    screen.onkey(r_paddle.up, "Up")
    screen.onkey(r_paddle.down, "Down")
    screen.onkey(l_paddle.up, "a")
    screen.onkey(l_paddle.down, "z")

    ball = Ball()
    scoreboard = Scoreboard()

    game_is_on = True
    while game_is_on:
        time.sleep(ball.ball_speed)
        screen.update()
        ball.move()

        # Detect wall collision
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce("y")

        # Detect paddle collision
        elif (330 <= ball.xcor() <= 340 and ball.distance(r_paddle) < 45
              or -340 <= ball.xcor() <= -330 and ball.distance(l_paddle) < 45):
            ball.bounce("x")

        # Detect miss
        if ball.xcor() > 380:
            scoreboard.update_score("l")
            ball.restart()
        elif ball.xcor() < -380:
            scoreboard.update_score("r")
            ball.restart()

        game_is_on = scoreboard.end_game()

    if screen.textinput("Play again?", "Type 'y' or 'n': ") == "y":
        screen.clear()
        start_game()
    else:
        return


start_game()

screen.exitonclick()
