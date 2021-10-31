#!/usr/local/bin/python

from datetime import date
from tkinter import *
import os
import time
import turtle
import random
import cv2

def turtle_cake():
    # sets background
    bg = turtle.Screen()
    bg.bgcolor("black")

    # Bottom Line 1
    turtle.penup()
    turtle.goto(-170,-180)
    turtle.color("white")
    turtle.pendown()
    turtle.forward(300)

    # Mid Line 2
    turtle.penup()
    turtle.goto(-160,-150)
    turtle.color("white")
    turtle.pendown()
    turtle.forward(275)

    # First Line 3
    turtle.penup()
    turtle.goto(-150,-120)
    turtle.color("white")
    turtle.pendown()
    turtle.forward(250)

    # Cake
    turtle.penup()
    turtle.goto(-100,-100)
    turtle.color("white")
    turtle.begin_fill()
    turtle.pendown()
    turtle.forward(140)
    turtle.left(90)
    turtle.forward(95)
    turtle.left(90)
    turtle.forward(140)
    turtle.left(90)
    turtle.forward(95)
    turtle.end_fill()

    # Candles
    turtle.penup()
    turtle.goto(-90,0)
    turtle.color("red")
    turtle.left(180)
    turtle.pendown()
    turtle.forward(20)

    turtle.penup()
    turtle.goto(-60,0)
    turtle.color("blue")
    turtle.pendown()
    turtle.forward(20)

    turtle.penup()
    turtle.goto(-30,0)
    turtle.color("yellow")
    turtle.pendown()
    turtle.forward(20)

    turtle.penup()
    turtle.goto(0,0)
    turtle.color("green")
    turtle.pendown()
    turtle.forward(20)

    turtle.penup()
    turtle.goto(30,0)
    turtle.color("purple")
    turtle.pendown()
    turtle.forward(20)

    # Decoration
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
    turtle.penup()
    turtle.goto(-40,-50)
    turtle.pendown()

    for each_color in colors:
        angle = 360 / len(colors)
        turtle.color(each_color)
        turtle.circle(10)
        turtle.right(angle)
        turtle.forward(10)

    turtle.penup()    
    turtle.goto(-200,-200)
    turtle.done()
      
def bdcard():
    image=cv2.imread('img/bdcard.png')

    while True:
        try:
            cv2.imshow("image", image)
            if cv2.waitKey(1)& 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break

        except KeyboardInterrupt:
            cv2.destroyAllWindows()
            break

today = date.today()
dob = date(2001, 11, 1) 	# This is indeed the date of your birthday.

birthday = date(today.year, dob.month, dob.day)
days_alive = (today-dob).days


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")
    time.sleep(4)
    print("Hey Shreya!")
    print("")
    time.sleep(4)
    print("I'm here to wish you a Happy Birthday from your friendly neighbourhood Cabin!")
    print("")
    time.sleep(4)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")
    print("Did you know that as of today, you are " + str(days_alive) + " days old")
    print("")
    time.sleep(4)
    print("wow that is amazing!")
    print("")
    time.sleep(4)
    print("If you wanted to stretch out those days in a single line,")
    time.sleep(2)
    print("Then it would look something like this: ")
    print("")
    time.sleep(3)
    
    for n in range(days_alive):
        print(n)
        time.sleep(0.002)
        if n == 69:
            print("\t lol 69 nice")
        
    time.sleep(4)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")
    print("Okay that was a lot of numbers, but dont worry as that number keeps on rising up.")
    print("")
    time.sleep(4)
    print("All it means is that each day you have another opportunity to strive to be better than the last!")
    print("")
    time.sleep(4)
    print("It's like a machine learning program. With each iteration, the program becomes better and better.")
    time.sleep(2)
    
    for n in range(10):
        print("and better")
        time.sleep(1)
        
    time.sleep(5)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")
    print("Aight, now here is a cake that is made by a turtle: ")
    print("")
    time.sleep(4)
    print("Please note: ONLY AS SOON AS the cake has been made, you can close the window to proceed.")
    print("")
    time.sleep(3)
    print("Afterwards, when the image pops up, you can press 'q' at any time to close the image.")
    print("")
    time.sleep(3)
    print("Return Back here once you are done.")
    print("")
    time.sleep(3)
    print("Im not the best programmer but I used this to experiment and understand programming a little better than before :D ")
    time.sleep(10)
    
    turtle_cake()
    bdcard()

    os.system('cls' if os.name == 'nt' else 'clear')
    print("")
    print("This is the end of this birthday wish. But i have also included a bonus script that should work if all goes well.")
    print("")
    time.sleep(4)
    print("Thank you for being yourself and cheers to a greater future!")
    print("")
    time.sleep(4)
