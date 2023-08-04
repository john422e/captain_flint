import pygame
from time import sleep

def playSound(fileName, channel, pan):
    # prep channel
    left, right = convertPan(pan)
    channel.set_volume(left, right)
    # prep sound
    sound = pygame.mixer.Sound(fileName)
    length = sound.get_length()
    # play it
    channel.play(sound)
    sleep(length)
    print("END OF SOUND")

def convertPan(panVal):
    """
    linear scaling panning
    expects a float between -1.0 and 1.0
    returns two floats as amps (0.0-1.0)
    """
    left = ((panVal * -1) + 1) * 0.5 # invert, put between 0 and 2, halve to get amp
    right = (panVal + 1) * 0.5 # put between 0 and 2, halve to get amp
    if left > 1: left = 1; right=0; print("LEFT EXCEEDED MAX VALUE. CAPPING AT -1")
    if right > 1: right = 1; left=0; print("RIGHT EXCEEDED MAX VALUE. CAPPING AT 1")
    print("LEFT:", left, "RIGHT:", right)
    return left, right
