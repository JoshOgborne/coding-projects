from gpiozero import LED, Buzzer, Button
from time import sleep

# Variables
red_led = LED(25)
amber_led = LED(8)
green_led = LED(7)
button = Button(2)
buzzer = Buzzer(15)
pressed = False
red_light_time = 3

# FUNCTIONS
# Light Functions
def stop():
    global pressed
    red_led.on()
    print('Red on')
    if pressed == False:
        sleep(3)
        sleep(red_light_time)
    else:
        padestrian_buzzer()
        sleep(red_light_time)
        pressed = False
    red_led.off()
    print('Red off')
    sleep(3)


def wait():

    amber_led.on()
    print('Amber on')
    sleep(3)
    print('Amber off')
    amber_led.off()


def go():
    green_led.on()
    print('Green on')
    sleep(6)
    print('Green off')
    green_led.off()

# Button Functions
def padestrian_buzzer():
    for i in range(15):
        buzzer.on()
        print('beep')
        sleep(0.1)
        buzzer.off()
        sleep(0.1)


def padestrian_cycle():
    print('Pressed')
    global pressed
    pressed = True


def cycle():
    while True:
        go()
        wait()
        stop()


# Main Program
button.when_activated = padestrian_cycle
cycle()

