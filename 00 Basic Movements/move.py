import subprocess

import RPi.GPIO as GPIO
import time
import nanocamera as nano
from PIL import Image
import sys

# Pin Definitions
output_pin1 = 18  # BCM pin 18, BOARD pin 12
output_pin2 = 23  # BCM pin 23, BOARD pin 16

output_pin3 = 24  # BCM pin 24, BOARD pin 18
output_pin4 = 25  # BCM pin 25, BOARD pin 22


def turn_right(turn_time):

    GPIO.output(output_pin1, GPIO.HIGH)
    time.sleep(turn_time)     
    GPIO.output(output_pin1, GPIO.LOW)


def turn_left(turn_time):

    GPIO.output(output_pin4, GPIO.HIGH)
    time.sleep(turn_time)     
    GPIO.output(output_pin4, GPIO.LOW)



def forward(running_time):

    GPIO.output(output_pin1, GPIO.HIGH)
    GPIO.output(output_pin4, GPIO.HIGH)
    time.sleep(running_time)
    GPIO.output(output_pin1, GPIO.LOW)
    GPIO.output(output_pin4, GPIO.LOW)
    


def reverse(running_time):    

    GPIO.output(output_pin2, GPIO.HIGH)
    GPIO.output(output_pin3, GPIO.HIGH)
    time.sleep(running_time)
    GPIO.output(output_pin2, GPIO.LOW)
    GPIO.output(output_pin3, GPIO.LOW)
    
    


def capture(i, running_time=0.5):
    

    camera = nano.Camera(flip=2, width=640, height=480, fps=30)
    frame = camera.read()
    print(type(frame))
    im = Image.fromarray(frame)
    im.save("imgs/" + str(i) + ".jpeg")
    camera.release()

    time.sleep(1)


def initialize():

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(output_pin1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(output_pin2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(output_pin3, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(output_pin4, GPIO.OUT, initial=GPIO.LOW)
    


def main(start):
    # Pin Setup:

    initialize()
    for i in range(start, start+5, 1):

        forward(0.5)
        capture(i)
        # time.sleep(6)
        
#    reverse(3)
#    time.sleep(0.5)
#        capture(i)
#        turn_right(0.55)
#        time.sleep(1)      
#        turn_left(0.525)
#        time.sleep(1)              

    
        


if __name__ == '__main__':

    start = int(sys.argv[1])
    print("start is: " + str(start))
    main(start)
