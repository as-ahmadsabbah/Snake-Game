from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.color("yellow")
        self.goto(0,260)
        self.hideturtle()
        self.write(f"Score: {self.score}",align="center",font=("moonspace",24,"normal"))

    def increase_score(self):
        self.clear()
        self.score +=1
        self.write(f"Score: {self.score}",align="center",font=("moonspace",24,"normal"))
        

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=("moonspace",24,"normal"))

    def return_game(self):
        self.goto(0,-15)
        self.write("To play again, press the R key",align="center",font=("moonspace",12,"normal"))

    def clr():
        Turtle.clear()