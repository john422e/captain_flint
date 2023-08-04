# std imports
from random import randrange
import time
from datetime import datetime, timedelta

# pi import
import RPi.GPIO as GPIO

# GLOBALS
TRIG = 23
ECHO = 24

pingInterval = 0.5 # in seconds


def ultrasonic_init():
    # initialize ultrasonic
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

    GPIO.output(TRIG, False)
    time.sleep(2)

def get_reading():
    # does a ping or something
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    break_loop = False
    timeout = datetime.now() + timedelta(seconds=1)

    pulse_end = 0
    pulse_start = 0

    # finds the time measurements?
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
        # if timeout > datetime.now():
        #    break;

    timeout = datetime.now() + timedelta(seconds=1)
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
        # if timeout > datetime.now():
        #     break;

    # some calculations to convert to centimeters
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    return round(distance, 2)
