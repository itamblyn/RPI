#flashing led code

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)

while True:
    GPIO.output(11, True)
    time.sleep(0.1)
    GPIO.output(11, False)
    time.sleep(0.1)

##########################################

#code for the button turning the led on and off

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.IN)
GPIO.output(11, False)
while True:
    input_value = GPIO.input(12)
    if input_value == False:
        print ("The button has been pressed. Lighting LED.")
        GPIO.output(11, True)
        time.sleep(2)
        GPIO.output(11, False)
        time.sleep(2)
        while input_value == False:
            input_value = GPIO.input(12)
        print ("the button has been released. Extinguishing LED")
    if input_value == True:
        GPIO.output(11, False)

