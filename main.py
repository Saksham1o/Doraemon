from turtle import *


# function for position
def my_goto(x, y):
    penup()
    goto(x, y)
    pendown()


# Function for drawing eyes
def eyes():
    fillcolor("#ffffff")
    begin_fill()
    tracer(False)
    a = 2.5
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a -= 0.05
            lt(3)
            fd(a)
        else:
            a += 0.05
            lt(3)
            fd(a)
    tracer(True)
    end_fill()


# Function for drawing whisker
def whisker():
    my_goto(-32, 135)
    seth(165)
    fd(60)
    my_goto(-32, 125)
    seth(180)
    fd(60)
    my_goto(-32, 115)
    seth(195)
    fd(60)
    my_goto(37, 135)
    seth(15)
    fd(60)
    my_goto(37, 125)
    seth(0)
    fd(60)
    my_goto(37, 115)
    seth(-13)
    fd(60)


# Function for drawing mouth
def mouth():
    my_goto(5, 148)
    seth(270)
    fd(100)
    seth(0)
    circle(120, 50)
    seth(230)
    circle(-120, 100)


# Function for drawing band
def band():
    fillcolor("#e70010")
    begin_fill()
    seth(0)
    fd(200)
    circle(-5, 90)
    fd(10)
    circle(-5, 90)
    fd(207)
    circle(-5, 90)
    fd(10)
    circle(-5, 90)
    end_fill()


# Function for drawing nose
def nose():
    my_goto(-10, 158)
    seth(315)
    fillcolor("#e70010")
    begin_fill()
    circle(20)
    end_fill()


# Functin for drawing black eyes
def black_eyes():
    seth(0)
    my_goto(-20, 195)
    fillcolor("#000000")
    begin_fill()
    circle(13)
    end_fill()

    pensize(6)
    my_goto(20, 205)
    seth(75)
    circle(-10, 150)
    pensize(3)

    # for drawing the white circle inside
    my_goto(-17, 200)
    seth(0)
    fillcolor("#ffffff")
    begin_fill()
    circle(5)
    end_fill()
    my_goto(0, 0)


# Function for drawing face
def face():
    fd(183)
    lt(45)
    fillcolor("#ffffff")
    begin_fill()
    circle(120, 100)
    seth(180)
    fd(121)
    pendown()
    seth(215)
    circle(120, 100)
    end_fill()
    my_goto(63.56, 218.24)
    seth(90)
    eyes()
    seth(180)
    penup()
    fd(60)
    pendown()
    seth(90)
    eyes()
    penup()
    seth(180)
    fd(64)


# Function for drawing head
def head():
    penup()
    circle(150, 40)
    pendown()
    fillcolor("#00a0de")
    begin_fill()
    circle(150, 280)
    end_fill()


# Combining all functions to one
def Doremon():
    head()
    band()
    face()
    nose()
    mouth()
    whisker()
