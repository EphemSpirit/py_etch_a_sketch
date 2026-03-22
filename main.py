from turtle import Turtle, Screen

jim = Turtle()

def move_forwards() -> None:
    jim.forward(10)

def move_backwards() -> None:
    jim.backward(10)

def rotate_clockwise() -> None:
    jim.setheading(jim.heading() - 20)

def rotate_anti_clockwise() -> None:
    jim.setheading(jim.heading() + 20)

def clear_drawing() -> None:
    jim.clear()
    jim.penup()
    jim.home()

screen = Screen()

screen.listen()

screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(rotate_anti_clockwise, "a")
screen.onkey(rotate_clockwise, "d")
screen.onkey(clear_drawing, "c")

screen.exitonclick()