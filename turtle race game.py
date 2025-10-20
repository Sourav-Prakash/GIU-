from turtle import Turtle,Screen
import random
l1=["orange","red","gold","magenta","green",]
ypos=[-70,-40,-10,20,50]
screen=Screen()
screen.bgcolor("brown")
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="make your bet",prompt="which turtle will win the race?,enter your colour:")
all_turtle=[]


is_raceon=False

for i in range(len(ypos)):
    tim=Turtle()
    tim.goto(x=-230,y=ypos[i])
    tim.color(random.choice(l1))
    tim.shape("turtle")
 
    all_turtle.append(tim)
if user_bet:
    is_raceon=True


while is_raceon:
    if tim.xcor()>230:
        is_raceon=False
        winningcolour=tim.pencolor()
        if user_bet==winningcolour:
            print(f"you have won,{winningcolour}wins!!")
        else:
            print(f"you have lost,{winningcolour} wins!!")
    for tim in all_turtle:
        randomdistance=random.randint(1,11)
        tim.forward(randomdistance)

screen=Screen()
screen.setup(width=500,height=500)

print(user_bet)
