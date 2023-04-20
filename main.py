from turtle import  Screen,Turtle 
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from PIL import Image


screen = Screen()


screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("My Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()

def clear_screan():
    snake.clr()
    scoreboard.clr()
    food.clr()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(clear_screan,"r")





game_is_on = True
while game_is_on:
    
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food)<15:
        food.refresh()
        scoreboard.increase_score()
        snake.create_Snake2()
    if snake.head.xcor()>290 or snake.head.xcor()<-295 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        game_is_on=False
        scoreboard.game_over()
        scoreboard.return_game()
    for seg in snake.segments :
        if seg == snake.head:
            pass
        elif snake.head.distance(seg)<10 :
            game_is_on=False            
            scoreboard.game_over()
            scoreboard.return_game()
#yes i did it ! my first game {AS}
screen.exitonclick()
