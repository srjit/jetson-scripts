import RPi.GPIO as GPIO

import time


output_pin1 = 18  # BCM pin 18, BOARD pin 12
output_pin2 = 23  # BCM pin 23, BOARD pin 16

output_pin3 = 24  # BCM pin 24, BOARD pin 18
output_pin4 = 25  # BCM pin 25, BOARD pin 22


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
