from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.listen()

tim.shape("turtle")
tim.color("red")

def move_forward():
    tim.forward(10)
def move_back():
    tim.back(10)
def move_right():
    tim.right(5)
    tim.forward(10)
def move_left():
    tim.left(5)
    tim.forward(10)
def clear():
    tim.penup()
    tim.goto(0, 0)
    tim.clear()
    tim.pendown()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=move_right)
screen.onkey(key="d", fun=move_left)
screen.onkey(key="c", fun=clear)


screen.exitonclick()