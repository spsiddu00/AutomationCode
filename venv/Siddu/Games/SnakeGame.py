import random
import turtle
import time
print("Imported")

screen = turtle.Screen()
screen.title("New Screen for Snake Game")
screen.bgcolor("green")
screen.setup(width=600,height=600)
screen.tracer(0)

#Shape up the Snake
head = turtle.Turtle()
head.speed(0)
head.color("black")
head.shape("circle")
head.goto(0,0)
head.penup()
head.direction = "STOP"

#Shape up the Snake Food
food = turtle.Turtle()
food.speed(0)
food.color("red")
food.shape("circle")
food.penup()
food.goto(0,100)



def go_Up():
    head.direction = "UP"
def go_Down():
    head.direction = "DOWN"
def go_Left():
    head.direction = "LEFT"
def go_Right():
    head.direction = "RIGHT"

def move():
    if(head.direction == "UP"):
        y = head.ycor()
        head.sety(y+20)
    if (head.direction == "DOWN"):
        y = head.ycor()
        head.sety(y - 20)
    if (head.direction == "LEFT"):
        x = head.xcor()
        head.setx(x - 20)
    if (head.direction == "RIGHT"):
        x = head.xcor()
        head.setx(x + 20)

# Keyboard Connection
screen.listen()
screen.onkeypress(go_Up,'Up')
screen.onkeypress(go_Down,'Down')
screen.onkeypress(go_Left,'Left')
screen.onkeypress(go_Right,'Right')

segments_List = []

#Main Loop
while True:
    screen.update()
    if(head.xcor()>290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290 ):
        head.direction = "STOP"
        time.sleep(1)
        head.goto(0,0)
        for x in segments_List:
            x.goto(1000,1000)
        segments_List.clear()
        food.goto(random.randint(-290, 290), random.randint(-290, 290))

    for elements in segments_List:
        if(head.distance(elements) < 20):
            head.direction = "STOP"
            time.sleep(1)
            head.goto(0, 0)
            for x in segments_List:
                x.goto(1000, 1000)
            segments_List.clear()
            food.goto(random.randint(-290, 290), random.randint(-290, 290))


    if(head.distance(food) <20):
        # Move the Food to different Position
        food.goto(random.randint(-290,290),random.randint(-290,290))

        # Add new new element to snake by creating new Turtile Object
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.color("gray")
        new_segment.shape("circle")
        new_segment.penup()
        segments_List.append(new_segment)

    if (len(segments_List) > 0):
        x = head.xcor()
        y = head.ycor()
        segments_List[0].goto(x, y)

    for i in range(len(segments_List) - 1, 0, -1):
        x = segments_List[i - 1].xcor()
        y = segments_List[i - 1].ycor()
        segments_List[i].goto(x, y)



    move()
    time.sleep(0.1)


# screen.mainloop()
print("End")