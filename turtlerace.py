from turtle import *
from random import randint



# FUNCTIONS
def race_track():
    ht()
    penup()
    goto(-140,140)
    for step in range(17):
        write(step)
        right(90)
        forward(10)
        pendown()
        for i in range(10):
            penup()
            forward(5)
            pendown()
            forward(10)
        penup()
        backward(160)
        left(90)
        forward(20)


def red_turtle():
    global ada
    ada = Turtle()
    ada.ht()
    ada.color('red')
    ada.shape('turtle')
    ada.penup()
    ada.goto(-160,100)
    ada.pendown()
    ada.st()
    for turn in range(36):
        ada.rt(10)


def blue_turtle():
    global bob
    bob = Turtle()
    bob.ht()
    bob.color('blue')
    bob.shape('turtle')
    bob.penup()
    bob.goto(-160,70)
    bob.pendown()
    bob.st()
    for turn in range(36):
        bob.rt(10)


def green_turtle():
    global ted
    ted = Turtle()
    ted.ht()
    ted.color('green')
    ted.shape('turtle')
    ted.penup()
    ted.goto(-160,40)
    ted.pendown()
    ted.st()
    for turn in range(36):
        ted.rt(10)


def yellow_turtle():
    global trt
    trt = Turtle()
    trt.ht()
    trt.color('purple')
    trt.shape('turtle')
    trt.penup()
    trt.goto(-160,10)
    trt.pendown()
    trt.st()
    for turn in range(36):
        trt.rt(10)


def turtles():
    red_turtle()
    blue_turtle()
    green_turtle()
    yellow_turtle()


def race():
    for turn in range(100):
        ada.forward(randint(1,6))
        bob.forward(randint(1,6))
        ted.forward(randint(1,6))
        trt.forward(randint(1,6))


def winner():
    if ada.xcor() >= bob.xcor() and ada.xcor() >= ted.xcor() and ada.xcor() >= trt.xcor():
        print(f'Red turtle won!')
        ada.penup()
        ada.goto(-225, 200)
        ada.pendown()
        for i in range(4):
            ada.forward(500)
            ada.right(90)
            ada.forward(300)
            ada.right(90)
    elif bob.xcor() >= ada.xcor() and bob.xcor() >= ted.xcor() and bob.xcor() >= trt.xcor():
        print(f'Blue Turtle won')
        bob.penup()
        bob.goto(-225, 200)
        bob.pendown()
        for i in range(2):
            bob.forward(500)
            bob.right(90)
            bob.forward(300)
            bob.right(90)
    elif ted.xcor() >= bob.xcor() and ted.xcor() >= ada.xcor() and ted.xcor() >= trt.xcor():
        print(f'Green Turtle won')
        ted.penup()
        ted.goto(-225, 200)
        ted.pendown()
        for i in range(2):
            ted.forward(500)
            ted.right(90)
            ted.forward(300)
            ted.right(90)
    elif trt.xcor() >= bob.xcor() and trt.xcor() >= ted.xcor() and trt.xcor() >= ada.xcor():
        print(f'Purple Turtle wins!')
        trt.penup()
        trt.goto(-225, 200)
        trt.pendown()
        for i in range(2):
            trt.forward(500)
            trt.right(90)
            trt.forward(300)
            trt.right(90)


def main():
    speed(0)
    race_track()
    turtles()
    race()
    winner()

# Main program
main()

exitonclick()