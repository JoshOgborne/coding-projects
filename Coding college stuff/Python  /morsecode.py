# Importing of libraries
from gpiozero import LED
from time import sleep

# Declaring variables
red_led = LED(17)
dot_time = 0.2
dash_time = dot_time * 3
character_space = dot_time * 3
word_space = dot_time * 7
menu = True

# Declaring functions
def make_morse_code(message):
    print(message)
    for letter in message:
        red_led.off()
        sleep(character_space)
        print(letter)
        print(CODE[letter.upper()])
        for dots in CODE[letter.upper()]:
            if dots == '.':
                dot()
            elif dots == '-':
                dash()
            else:
                sleep(word_space)


def dot():
    print('dot')
    red_led.on()
    sleep(dot_time)
    red_led.off()
    sleep(dot_time)


def dash():
    print('dash')
    red_led.on()
    sleep(dash_time)
    red_led.off()
    sleep(dot_time)


# Creating dictionary of morse code
CODE = {' ': ' ',
        "'": '.----.',
        '(': '-.--.-',
        ')': '-.--.-',
        ',': '--..--',
        '-': '-....-',
        '.': '.-.-.-',
        '/': '-..-.',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ':': '---...',
        ';': '-.-.-.',
        '?': '..--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '_': '..--.-'}


# main program
print("Welcome to my program")
while menu == True:
    question = input("Do you want to translate? ")
    question = question.upper()
    if question == 'Y':
        sentence = input("Type Message ")
        make_morse_code(sentence)
    elif question == 'N':
        menu = False
        print('Bye')
    else:
        print('y/n')

