import subprocess
import random
import string

import RPi.GPIO as GPIO
import time

import nanocamera as nano
from PIL import Image
import sys

import os

import warnings
warnings.filterwarnings("ignore")

import decision_engine


# Pin Definitions
output_pin1 = 18  # BCM pin 18, BOARD pin 12
output_pin2 = 23  # BCM pin 23, BOARD pin 16

output_pin3 = 24  # BCM pin 24, BOARD pin 18
output_pin4 = 25  # BCM pin 25, BOARD pin 22

character_limit = 5


def turn_right(turn_time):

    GPIO.output(output_pin1, GPIO.HIGH)
    GPIO.output(output_pin3, GPIO.HIGH)

    time.sleep(turn_time)     

    GPIO.output(output_pin1, GPIO.LOW)
    GPIO.output(output_pin3, GPIO.LOW)


def turn_left(turn_time):

    GPIO.output(output_pin2, GPIO.HIGH)
    GPIO.output(output_pin4, GPIO.HIGH)

    time.sleep(turn_time)     

    GPIO.output(output_pin2, GPIO.LOW)
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


def stop():

    GPIO.output(output_pin1, GPIO.LOW)
    GPIO.output(output_pin2, GPIO.LOW)
    GPIO.output(output_pin3, GPIO.LOW)
    GPIO.output(output_pin4, GPIO.LOW)    
    


def capture():
    
    camera = nano.Camera(flip=0, width=640, height=480, fps=30)
    frame = camera.read()
    im = Image.fromarray(frame)
    camera.release()
    return im


def initialize():

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(output_pin1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(output_pin2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(output_pin3, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(output_pin4, GPIO.OUT, initial=GPIO.LOW)
    


def main():
    
    # Pin Setup:
    initialize()

    for i in range(20):

        print("Making next decision...")

        stop()
        image = capture()
        next = decision_engine.next_move(image)

        print("Decision: ", next)

        if next == 'forward':
            forward(0.4)
        elif next == 'turn_left':
            forward(1.3)
            turn_left(.73)
        elif next == 'turn_right':
            turn_right(0.95)
        elif next == 'reverse':
            reverse(1)
            turn_left(0.7)
            stop()

        


if __name__ == '__main__':

    main()
