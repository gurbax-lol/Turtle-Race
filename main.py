from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bet!", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "green", "blue", "purple", "brown"]
y_axis = -80
turtle_racers = []

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_axis)
    turtle_racers.append(new_turtle)
    y_axis += 40

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_racers:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"Congrats, you've won! The {winning_turtle} turtle won the race!")
            else:
                print(f"Sorry, you've lost! The {winning_turtle} turtle won the race!")
        random_distance = randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
