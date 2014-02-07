#!/usr/bin/env python


import time              # get the time library so we can read the clock
import RPi.GPIO as GPIO  # same with the GPIO library 
GPIO.setmode(GPIO.BOARD) # tell the hardware to get ready
GPIO.setup(12, GPIO.IN)  # tell the GPIO that pin 12 will be used for input  

while True: # run forever (you can kill this code with CTRL and C together 

    input_value = GPIO.input(12) # read the value of the pin (it will be True or False)

    t = time.time() # write down the time you made the measurement 

    if input_value == False: # someone was pushing the button 
        p = 1
        print t, p

    else: # nothing was pushing the button
        p = 0
        print t, p

    time.sleep(0.001) # wait a little while before you check again
                      # if you remove this line, the Pi will keep looping as fast as possible, which is useful sometimes


