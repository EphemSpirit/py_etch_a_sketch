# Turtle Event Listeners
# Turtle listen() starts the turtle listening for user events
from turtle import Turtle, Screen

jim = Turtle()




def move_forwards() -> None:
    jim.forward(10)



screen = Screen()
# tell screen to start listening and bind a function to a key press
screen.listen()
screen.onkey(move_forwards, "space")
screen.exitonclick()