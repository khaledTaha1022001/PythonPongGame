import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import  Ball
from scoreboard import Score
screen= Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0) # to turn off the animation , as a result we need to keep updating the screen using while ...
right_score=Score(x_pos=100,y_pos=200)
left_score= Score(x_pos=-100,y_pos=200)
ball= Ball()

rightpaddle= Paddle(350,0)
leftpaddle= Paddle(-350,0)







screen.listen()
screen.onkey(rightpaddle.go_up,"Up")
screen.onkey(rightpaddle.go_down,"Down")
screen.onkey(leftpaddle.go_up,"w")
screen.onkey(leftpaddle.go_down,"s")

game_is_on= True


while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    #detect the collision with the wall
    if ball.ycor()>280 or ball.ycor()<-280:
        #needs to bounds
        ball.bounce_y()
    #detect collision with right paddle
    if ball.distance(rightpaddle)<50 and ball.xcor()>320 or ball.distance(leftpaddle)<50 and ball.xcor()<-320:
        ball.bounce_x()
    if ball.xcor()>380:
        ball.reset_position()
        left_score.Scorerefresh()
    if ball.xcor()<-380:
        ball.reset_position()
        right_score.Scorerefresh()








screen.exitonclick()