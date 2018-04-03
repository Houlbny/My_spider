import turtle
import random
import datetime

random.seed(datetime.datetime.now())

# this helps me import the turtle and random moudles that i will use in this assignment

numTurtles = 40
turtles = []
position = set()


def initialTurtlePosition():
    global position
    for turtle in turtles:
        turtle.shape("circle")
        turtle.shapesize(0.5)
        turtle.penup()
        turtle.goto(random.randrange(-200, 200, 20), random.randrange(-200, 200, 20))
        position.add(turtle.pos())
        # print(position)


for x in range(numTurtles):
    turtles.append(turtle.Turtle())

initialTurtlePosition()

# this function aims to generate a range of turtles in random position

position = list(position)
print(position)


def collision_detection():
    directions = [0, 90, 180, 270]
    turtle.setheading(random.choice(directions))
    turtle.color("yellow")
    turtle.shape("circle")
    turtle.shapesize(0.5)
    step = 20
    while (True):
        # turtle.penup()
        if abs(turtle.pos()[0]) > 200 or abs(turtle.pos()[1]) > 200:
            turtle.penup()
            turtle.goto(0, 0)
            turtle.pendown()
        else:
            turtle.setheading(random.choice(directions))
            turtle.fd(step)
            if turtle.pos() in position:
                turtle.backward(step)
                print("back")
                continue


collision_detection()

#  this function aims to inplement collision detection. when a randomly moving turtle encounter with another turtle in random position
#  when a randomly moving turtle encounter with another turtle in random position it will move backward to evade collision