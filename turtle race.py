from turtle import Turtle, Screen
import random

# setting up the screen
screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race ? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-100 , -60, -20, 20, 60, 100]
all_turtles = []

for turtle_index in range (0,6):
    timmy = Turtle(shape="turtle")
    timmy.color(colors[turtle_index])
    timmy.penup()
    timmy.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(timmy)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print (f" You've Won! {winning_color} turtle is the Winner! ")
            else:
                print(f" You've Lost! {winning_color} turtle is the Winner! ")

        rand_distance = random.randint(0, 10)
        turtle.forward((rand_distance))

screen.exitonclick()
