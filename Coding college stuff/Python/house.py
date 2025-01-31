from turtle import *


# Declaring Variables
width = 50
length = width * 2
menu =True


# DEFINING FUNCTIONS
# Default start for each function
def start_pos():
    penup()
    goto(-100,-100)
    pendown()

# Actual functions
def rectangle():
    fillcolor('grey')
    begin_fill()
    for i in range(2):
        forward(length)
        left(90)
        forward(width)
        left(90)
    end_fill()


def roof():
    fillcolor('red')
    begin_fill()
    right(30)
    forward(length)
    right(120)
    forward(length)
    end_fill()
    start_pos()

def door():
    forward(length/2 - (length/12))
    fillcolor('orange')
    begin_fill()
    left(90)
    for x in range(2):
        forward(length/4)
        right(90)
        forward(length/6)
        right(90)
    end_fill()
    forward(length/8)
    right(90)
    penup()
    forward(length/20)
    pendown()
    fillcolor('black')
    begin_fill()
    circle(length/50)
    end_fill()
    start_pos()

def window():
    penup()
    forward(length/4)
    left(90)
    forward(width - (width/2))
    pendown()
    for t in range(2):
        begin_fill()
        for i in range(4):
            fillcolor('white')
            forward(width/4)
            left(90)
        end_fill()
        penup()
        right(90)
        forward(length/2)
        pendown()
    start_pos()
    left(90)

def cloud():
    penup()
    goto(length * 2, length)
    pendown()
    fillcolor('white')
    begin_fill()
    for i in range(6):
        for t in range(120):
            forward(width/200)
            right(1)
        left(60)
    end_fill()

def sun():
    penup()
    goto(length * -2,length)
    pendown()
    fillcolor('yellow')
    begin_fill()
    for i in range(12):
        left(120)
        forward(width)
        left(120)
        forward(width)
        right(90)
    end_fill()
    start_pos()


def grass():
    penup()
    goto(-1000,-100)
    pendown()
    right(60)
    fillcolor('green')
    begin_fill()
    for i in range(180):
        left(120)
        forward(width/5)
        right(120)
        forward(width/5)
    right(30)
    for i in range (4):
        forward(6000)
        right(90)
    end_fill()



# Main  function
def main():
    bgcolor('blue')
    speed(0)
    start_pos()
    rectangle()
    left(90)
    forward(width)
    roof()
    left(60)
    door()
    sun()
    window()
    cloud()
    grass()

# Main program
while menu == True:
    question = textinput('Choose picture size','Do you want a small(s), medium(m) or large(l) picture? or type (x) to exit ')
    clearscreen()
    if question == 's':
        width = 50
        length = width*2
        main()
    elif question == 'm':
        width = 75
        length = width*2
        main()
    elif question == 'l':
        width = 100
        length=width*2
        main()
    elif question == 'x':
        menu = False
    else:
        'Please put s, m, l, or x'

