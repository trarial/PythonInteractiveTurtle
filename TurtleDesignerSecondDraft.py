import turtle
from turtle import*
import math
import time
import random


######## DEFINITION SPACE


def explanation():
    """A tutorial! How fun."""

    response = input("""\n\n\n\n\n
#########################################################            
#                                                       #
#        Welcome to Turtle Pattern Designer!            #
#                                                       #
#  Would you like an explanation of what's to follow?   #
#  ([y] or [yes] to continue, ENTER to skip)            #
#                                                       #
#########################################################
\n""")
    if response in ('y', 'Y', 'ye', 'YE', 'Ye', 'yE', 'yes', 'YES'):
        input("""\n\n\n\
###################################################################

In this script, you will be choosing what instructions to pass to 

your "turtle", or the computer's pen. You will choose what color the

trail the turtle leaves behind is, how far he moves, and so on.
    
    (ENTER to continue)
    
###################################################################\n\n\n""")
        print("""\
###################################################################\n""")
        input("""\
Make sure to read each prompt carefully, inputting either numbers or

words and confirming your choice with ENTER.
    
    (ENTER to continue)
    
###################################################################\n\n\n""")
        print("""\
###################################################################\n""")
        input("""\
The toughest part to understand at first is the turtle's/pen's 

heading. It'simportant to remember that -the angle of 

turning is relative to the turtle itself-, not relative to 

your view of the screen. So telling him to turn left by 45 degrees

twice means he would be pointing straight up after he finishes moving.

    (ENTER to continue)
    
###################################################################\n\n\n""")
        print("""\
###################################################################\n""")
        input("""\
Otherwise, this script is all about experimentation and trial and error--

Everythihng should become clear after a few runs through!
    
    (ENTER to begin)

###################################################################\n\n\n\n\n""")

    else:
        pass


def turtle_cycle(turtle, fwrd, angles):
    """What actually moves the turtle. This is repeated with <for> later."""

    xangle = 0
    iterations = len(angles)
    for i in range(iterations):
        turtle.forward(fwrd)
        turtle.left(angles[xangle])
        xangle = xangle + 1


def turtle_cycle_input():
    """Gets a number of angles from the user according to a value they chose."""

    anglelist = []
    turns = input("""\n
How many times do you want your turtle to turn in each cycle?\n""")
    turns = check_if_int(turns)
    turns = int(turns)
    for i in range(turns):
        stri = str(i + 1)
        x = input("""\n
What would you like the value of angle """ + stri + """ to be?\n""")
        x = check_if_int(x)
        x = int(x)
        anglelist.append(x)
    return anglelist

    
    #### Checks if user input is within allowed range. ####
def error(x, l1, admonish = """\n
The program doesn't quite understand what you said. Try sticking
to the colors of the rainbow\n"""):    
    try:
        int(x)
    except:
        while x not in l1:
            print()
            x = input(admonish)
            print()
        return x
    else:
        while x not in l1 and int(x) not in l1:
            print()
            x = input(admonish)
            print()
        return x
    
    #### Checks if the user input can be smoothly converted to an integer####
def check_if_int(x, admonish = """\n
It seems as if you've entered some non-numeric characters. Please try again.\n"""):    
    try:
        int(x)
    except:
        newx = input(admonish)
        check_if_int(newx, admonish)
        x = newx
    return x


def default(func_name, default_value):
    """Assigns a value to a variable if the user presses ENTER."""

    if func_name == None or func_name == '':
        func_name = default_value
        return func_name
    return func_name


def color_choice():
    """User input: Solid color or gradient?"""

    choice_char = input("""\n
Would you like a solid color for your turtle's drawn trail?

Or would you prefer it to cycle through colors?

Press [s] for solid, [g] for gradient.\n\n""")
    if choice_char in ('S', 's'):
        turtcol = input("Choose a color for your turtle, or hit enter for default white\n")
        turtcol = default(turtcol, "white")
        turtcol = error(turtcol, ('red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black', 'white'))
        return None, None, None, None, None, None, 0, turtcol
    
    else:
        r, g, b, rc, gc, bc = gradient_func()
        return r, g, b, rc, gc, bc, 1, None


############################### MAIN EXECUTION FUNCTION ########################

def main():
    switch = 1

    bg = input("""\n
Choose background color, or hit enter to use default (black).

Hint: Choose simple colors, like yellow, white, red, green.\n\n""")
    bg = default(bg, "black")    
    bg = error(bg, ['black', 'white', 'red', 'pink', 'green', 'lightgreen', 'hotpink', 'yellow', 'orange', 'purple', 'blue'], """\n
The program doesn't quite understand what you just said. Sticking to the
rainbow might help you.\n""")


    #how fast goes here
    #pen thickness
    #visible turtle


    r, g, b, rc, gc, bc, switch, turtcol = color_choice()


    zoomfac = input("""\n
Pick a number between 0 and 10--

this will be the factor by which the screen size will be

determined. Default is 1, which should be good for most purposes.\n\n""")
    zoomfac = default(zoomfac, 1)
    zoomfac = check_if_int(zoomfac)
    zoomfac = error(str(zoomfac), ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'), """\n
You've entered a number outside of the given range (for the mathematically
inclined, that range is 0 < x <= 10).
Please try again.\n""")
    zoomfac = int(zoomfac)


    fwrd = input("""\n
How far forward would you like your turtle to move

before each angle change? This number will be the number of pixels

the turtle moves before changing direction. As a reference point,

if you chose the default screen size factor of '1', the screen

is about 500 pixels wide. 

This defaults to 50.\n\n""")
    fwrd = default(fwrd, 50)
    fwrd = check_if_int(fwrd)
    fwrd = int(fwrd)


    anglelist = turtle_cycle_input()


    iteration = input("""\n
How much should be added to how far forward your 

turtle moves upon each cycle? In other words, how

fast do you want your design to grow?

This defaults to 1.\n\n""")
    iteration = default(iteration, 1)
    iteration = check_if_int(iteration)
    iteration = int(iteration)


    cycle_number = input("""\n
How many times would you like your turtle to follow
the above directions?\n\n""")
    cycle_number = default(cycle_number, 30)
    cycle_number = check_if_int(cycle_number)
    cycle_number = int(cycle_number)


    input("""\n\n
Once the drawing is finished, close the turtle window to get the
option to try again with new settings.

[Press ENTER to continue]\n""")
    

    ######## SCREEN AND TURTLE INIT

    negx, negy, posx, posy = windfunc(zoomfac)

    wn = turtle.Screen()
    colormode(255)
    wn.bgcolor(bg)
    wn.title("Turtle")

    wn.setworldcoordinates(negx, negy, posx, posy)

    t1 = turtle.Turtle()
    #t2 = turtle.Turtle()
    #t3 = turtle.Turtle()
    #t4 = turtle.Turtle()

    t1.speed("fastest")
    #t2.speed("fastest")
    #t3.speed("fastest")
    #t4.speed("fastest")

    t1.pensize(1)
    if switch == 0:
        t1.color(turtcol)
    show_turtle(t1, 'no')

    ####    
    

    if switch == 1:
        r, g, b, rc, gc, bc = int(r), int(g), int(b), int(rc), int(gc), int(bc)
    
    for q in range(cycle_number):
        if switch == 1:
            r, g, b = col_cycler(r, rc, g, gc, b, bc)
            r1, g1, b1 = abs(r), abs(g), abs(b)
            t1.color(r1, g1, b1)
        turtle_cycle(t1, fwrd, anglelist)
        fwrd = fwrd + iteration

    wn.mainloop()
    again_func()

################################################################################


def col_cycler(r, rc, g, gc, b, bc):
    """Works with the gradient values to alter the pen color."""

    r = r + rc
    g = g + gc
    b = b + bc
    if r >= 255:
        r = -255
    if g >= 255:
        g = -255
    if b >= 255:
        b = -255
    return r, g, b


def windfunc(fac):
    """Adjusts window to a single factor, default 1"""

    negx = -550 * fac
    negy = -475 * fac
    posx = 550 * fac
    posy = 475 * fac
    return negx, negy, posx, posy


def color_changer(r=None, g=None, b=None):
    """For creating smooth gradients"""

    if r != None:
        r = r + 1
        if r >= 255:
            r = -255
    if g != None:
        g = g + 1
        if g >= 255:
            g = -255
    if b != None:
        b = b + 1
        if b >= 255:
            b = -255
    return r, g, b


def color_assign(r, g, b):
    """To pass abs rgb values"""

    return abs(r), abs(g), abs(b)


def show_turtle(turtle, x):
    """Do you want to see the turtle?"""

    if show_turtle == 'yes':
        turtle.showturtle()
    else:
        turtle.hideturtle()


def simple_increment(x, incr):
    """Makes something change by something-else-many"""

    x = x + incr
    return x


def again_func():
    """Prompts user whether they want to re-run the program."""

    again = input("""\
Would you like to create another? [y/n]\n""")
    if again in ('Y', 'y', 'YE', 'ye', 'yE', 'Ye', 'yes', 'YES'):
        main()
    else:
        print()
        print("Alright! Closing pattern creator.\n")


def gradient_func():
    """User is routed here when they select to create a gradient. Takes input."""

    red = input("""\n
For choosing the color to start with, and choosing how to cycle through

through a gradient, first choose three values for the starting color. For each,

choose a value between 0 and 255. This will determine the intensity of each color. When all

colors are at 255, you have a white turtle trail. when all colors are at 0, you have a 

black turtle trail. First, choose the value for red:\n\n""")
    red = check_if_int(red)
    red = error(int(red), range(256), "\nEnter a number between 0 and 255:\n")
    green = input("\nNow, green:\n")
    green = check_if_int(green)
    green = error(int(green), range(256), "\nEnter a number between 0 and 255:\n")
    blue = input("\nAnd blue:\n")
    blue = check_if_int(blue)
    blue = error(int(blue), range(256), "\nEnter a number between 0 and 255:\n")
    redcyc = input("""\n
Now, choose a value for each color that will determine how quickly the gradient will

cycle through it-- so, 10 would increase the value of a color (remember, the number between 0

and 255,) by 10 every iteration of the turtle's path, and 0 would mean that particular

color would not change intensity at all. 


So first choose the cycle frequency for red:\n\n""")
    redcyc = check_if_int(redcyc)
    greencyc = input("\nAnd similarly for green:\n")
    greencyc = check_if_int(greencyc)
    bluecyc = input("\nAnd blue:\n")
    bluecyc = check_if_int(bluecyc)
    return red, green, blue, redcyc, greencyc, bluecyc


#### END DEFINITION SPACE



######## EXECUTION

explanation()
main()

####
