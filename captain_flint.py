import subprocess
import RPi.GPIO as GPIO
from time import sleep

# setup
filename = "pieces_of_eight.wav"
command = 'aplay'

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2, GPIO.OUT) # initialize to 'off'

print('on')
GPIO.output(2, True)
subprocess.call(['afplay', filename])

sleep(2)

print('off')
GPIO.output(2, False)
