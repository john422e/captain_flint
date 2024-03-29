# standard imports
import socket, argparse, random, time, subprocess

import pathlib

from datetime import datetime, timedelta

# pi import
#import RPi.GPIO as GPIO

# osc imports
#from pythonosc import dispatcher, osc_server, osc_message_builder, udp_client

TRIG = 23
ECHO = 24

"""
def ultrasonic_init():
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


# setup
filename = "pieces_of_eight.wav"
command = 'aplay'

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#
# initialize control switch for control relay
GPIO.setup(2, GPIO.OUT) # initialize to 'off'
# initialize sensor pins
ultrasonic_init()

def pieces_of_eight():
    print('on')
    GPIO.output(2, True)
    subprocess.call([command, filename])

def turn_off():
    print('off')
    GPIO.output(2, False)
"""



# create path objects to audio files directory
audioDir = str(pathlib.Path.cwd()) + "/audio/"
audioDir = pathlib.Path(audioDir)
# convert to list and store audio file strings
audioFiles = list(audioDir.iterdir())

# set to False for linux
osx = True

def getRandomAudioFile(fileList):
    fn = random.choice(fileList)
    return fn

def playAudio(filename):
    if osx:
        command = 'afplay'
    else:
        command = 'aplay' # for linux

    subprocess.call([command, filename])

trigger_thresh = 70

while True:
    reading = 0#get_reading()
    print(reading)
    if reading <= trigger_thresh:
        print('triggered')
        playAudio(random.choice(audioFiles))
        #pieces_of_eight()
        time.sleep(3)
        #turn_off()
    time.sleep(1.01)
