import pigo
import time
import random
from gopigo import *

'''
This class INHERITS your teacher's Pigo class. That means Mr. A can continue to
improve the parent class and it won't overwrite your work.
'''


class GoPiggy(pigo.Pigo):
    # CUSTOM INSTANCE VARIABLES GO HERE. You get the empty self.scan array from Pigo
    # You may want to add a variable to store your default speed
    MIDPOINT = 90
    STOP_DIST = 20

    # CONSTRUCTOR
    def __init__(self):
        print("Piggy has be instantiated!")
        # this method makes sure Piggy is looking forward
        self.calibrate()
        # let's use an event-driven model, make a handler of sorts to listen for "events"
        while True:
            self.stop()
            self.handler()

    ##### HANDLE IT
    def handler(self):
        ## This is a DICTIONARY, it's a list with custom index values
        # You may change the menu if you'd like
        menu = {"1": ("Navigate forward", self.nav),
                "2": ("Rotate", self.rotate),
                "3": ("Dance", self.dance),
                "4": ("Calibrate", self.calibrate),
                "s": ("Check status", self.status),
                "q": ("Quit", quit)
                }
        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])
        #
        ans = input("Your selection: ")
        menu.get(ans, [None, error])[1]()

    # A SIMPLE DANCE ALGORITHM
    def dance(self):
        print("Piggy dance")
        ##### WRITE YOUR FIRST PROJECT HERE
        print("Is it clear?")
        for x in range(3):
            if not self.isClear():
                print "Omgorsh, it's not safe!"
                break
            x = 100
            print('Speed is set to: ' + str(x))
            set_speed(x)
            servo(20)
            self.encB(7)
            self.encR(2)
            self.encL(2)
            self.encF(15)
            servo(120)
            time.sleep(.1)
            x += 25

    def status(self):
        print("My power is at "+ str(volt()) + " volts")
        self.encF(18)



    # AUTONOMOUS DRIVING
    def nav(self):
        print("Piggy nav")
        ##### WRITE YOUR FINAL PROJECT HERE
        #TODO: If while loop fails, check for other paths

        #loop: check that it's clear
        while self.isClear():
            #let's go forward just a little bit
            self.encF(10)


####################################################
############### STATIC FUNCTIONS

def error():
    print('Error in input')


def quit():
    raise SystemExit


####################################################
######## THE ENTIRE APP IS THIS ONE LINE....
g = GoPiggy()
