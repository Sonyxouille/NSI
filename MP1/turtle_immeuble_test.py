from turtle import * # type: ignore
from random import * # type: ignore

setup(1920,1080,0,0)

def fond():
    up()
    goto(1000,1000)
    fillcolor('deepskyblue3')
    begin_fill()
    goto(1000,-1000)
    goto(-1000,-1000)
    goto(-1000,1000)
    goto(1000,1000)
    end_fill()

def cloud():
    up()
    h = heading()
    x = 0
    y = 280
    goto(x,y)
    down()
    fillcolor('white')
    begin_fill()
    goto(x+88,y)
    angle = 90
    for i in range(0,4):
        circle(15,90)
        angle += 15
        setheading(angle)
    angle = 90
    up()
    goto(x,y)
    setheading(180)
    angle = 90
    down()
    for i in range(0,4):
        circle(-15,90)
        angle -= 15
        setheading(angle)
    end_fill()

down()
hideturtle()
speed(100000)
fond()
#quartier(-300,-100)
cloud()
done()


