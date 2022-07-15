from turtle import  Turtle

class Score(Turtle):
    def __init__(self,x_pos,y_pos):
        super().__init__()
        self.color("white")
        self.score=0
        self.hideturtle()
        self.penup()
        self.goto(x=x_pos,y=y_pos)
        self.write(f"Score: {self.score}",align="center",font=("Arial", 24, "normal"))

    def Scorerefresh(self):
        self.clear()
        self.score+=1
        self.write(f"Score: {self.score}",align="center",font=("Arial", 24, "normal"))
