# standard imports
from random import randrange, choice
from time import sleep

# non-standard imports
import pathlib, pygame
# my modules
import audioFunctions as af

runningOnPi = True # set to False for demoing on desktop
if runningOnPi:
    import sensorFuncs as sensor

# collect audio files
audioDir = str(pathlib.Path.cwd()) + "/audio/wavs/"
audioDir = pathlib.Path(audioDir)
# convert to list and store audio file strings
audioFiles = list(audioDir.iterdir())
# only keep the wav files
audioFiles = [f for f in audioFiles if str(f).split('.')[-1]=='wav']

# initiate sensor
if runningOnPi:
    sensor.ultrasonic_init()

# initiate mixer
pygame.mixer.init()
channel1 = pygame.mixer.Channel(0)
#channel1.set_volume(1.0, 0.0)
channel2 = pygame.mixer.Channel(1)
#channel2.set_volume(0.0, 1.0)

cpt_on = True

# start up sound
startSound = None
for f in audioFiles:
    if "pieces_of_eight" in str(f):
        startSound = str(f)

if startSound:
    print("START UP")
    af.playSound(startSound, channel1, -1.0)

# MAIN LOOP
while cpt_on:
    # get sensor reading
    if runningOnPi:
        reading = sensor.get_reading()
    else:
        reading = randrange(1000)
    print("READING", reading)
    if reading > 10 and reading < 110:
        print("TRIGGER SOUND")
        # if triggered, play random sound file
        audioFile = str(choice(audioFiles))
        af.playSound(audioFile, channel1, -1.0) # filename, channel, pan value
        sleep(0.5) # add a short buffer delay

    #pygame.mixer.quit()
    #cpt_on = False

# shut down/clean up
