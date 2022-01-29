import time
import turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
s = turtle.Screen()
s.setup(width=800, height=600)
s.bgcolor("black")
s.title("Ping-Pong")
s.tracer(0)
paddle1 = Paddle(0)
paddle2 = Paddle(1)
ball = Ball()
scoreboard = Scoreboard()
s.listen()
s.onkey(paddle1.up, "Up")
s.onkey(paddle1.down, "Down")
s.onkey(paddle2.w, "w")
s.onkey(paddle2.s, "s")
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    s.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle1) < 50 and ball.xcor() > 340:
        ball.bounce_x()

    if ball.distance(paddle2) < 50 and ball.xcor() < -350:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        if scoreboard.l_score < 5:
            scoreboard.l_score += 1
            scoreboard.update_scoreboard()
        elif scoreboard.l_score == 5:
            scoreboard.goto(0, 100)
            scoreboard.update_scoreboard()
            scoreboard.write("Player-1 WON", align="center",
                             font=("Arial", 25, "normal"))
            game_is_on = False

    if ball.xcor() < -380:
        ball.reset_position()
        if scoreboard.r_score < 5:
            scoreboard.r_score += 1
            scoreboard.update_scoreboard()
        elif scoreboard.r_score == 5:
            scoreboard.goto(0, 100)
            scoreboard.update_scoreboard()
            scoreboard.write("Player-2 WON", align="center",
                             font=("Arial", 25, "normal"))
            game_is_on = False
s.exitonclick()
