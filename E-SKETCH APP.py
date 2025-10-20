from turtle import Turtle,Screen

tinny=Turtle()

def move_forward():
    tinny.forward(12)

def move_backward():
    tinny.backward(12)

def change_square():
    tinny.shape("square")

def change_circle():
    tinny.shape("circle")
def turn_left():
    tinny.left(90)

def turn_right():
    tinny.right(90)

screen=Screen()
screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_backward,"s")
screen.onkey(change_square,"e")
screen.onkey(change_circle,"c")
screen.onkey(turn_left,"q")
screen.onkey(turn_right,"u")
