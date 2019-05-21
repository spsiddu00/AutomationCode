import random
import turtle
import time
print("Imported")

screen_width = 600
screen_height = 600

screen = turtle.Screen()
screen.title("New Screen for Snake Game")
screen.bgcolor("green")
screen.setup(width=screen_width,height=screen_height)
screen.tracer(0)

#Shape up the Snake
stick = turtle.Turtle()
stick.speed(0)
stick.penup()
stick.color("black")
stick.shape("square")
stick.shapesize(stretch_wid=1, stretch_len=5)
stick.goto(-screen_width/4,-screen_height/4)
stick.direction = "STOP"

#Shape up the Snake Food
bal = turtle.Turtle()
bal.speed(0)
bal.color("red")
bal.shape("circle")
bal.penup()
bal.goto(0,100)


def left():
    stick.direction = "LEFT"

def right():
    stick.direction = "RIGHT"

screen.listen()
screen.onkeypress(left,'Left')
screen.onkeypress(right, 'Right')

    
def Stick_move():
    if(stick.direction == "LEFT"):
        x = stick.xcor()
        stick.setx(x - 20)
    if (stick.direction == "RIGHT"):
        x = stick.xcor()
        stick.setx(x + 20)

def ball_Move():
    

while True:
    screen.update()
    if(stick.xcor() < -290):
        stick.setx(-290)
    if(stick.xcor() > 290):
        stick.setx(290)

    Stick_move()
    time.sleep(0.06)

