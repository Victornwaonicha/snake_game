from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("cyan")
screen.title("The Snake Game")


starting_position = [(0, 0), (-20, 0), (-41, 0)]

for position in starting_position:
    snakes = Turtle(shape="square")
    snakes.goto(position)

















screen.exitonclick()
