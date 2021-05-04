from turtle import Turtle



class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=5 , stretch_len=1)
        self.penup()
    def move_up(self):
        y_cor = self.ycor() + 20
        self.goto(self.xcor() , y_cor)

    def move_down(self):
        y_cor = self.ycor() - 20
        self.goto(self.xcor() , y_cor)


    
        



# screen.update()







