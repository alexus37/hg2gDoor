#!/usr/bin/python
import os
import RPi.GPIO as GPIO
import time
import pygame
from random import randint

def play_sound(file_name, vol=100.0):
    pygame.mixer.init()
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.load(file_name)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

# Set Broadcom mode so we can address GPIO pins by number.
GPIO.setmode(GPIO.BCM)

# consts
DIR = os.path.dirname(os.path.abspath(__file__))
DOOR_SENSOR_PIN = 18
NUMBER_OF_AUDIO_FILES = len([name for name in os.listdir(f'{DIR}/audio/') if os.path.isfile(f'{DIR}/audio/{name}')])
print(f'Found {NUMBER_OF_AUDIO_FILES} mp3 files')


isOpen = False
oldIsOpen = False

# Set up the door sensor pin.
GPIO.setup(DOOR_SENSOR_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while True:
    oldIsOpen = isOpen

    isOpen = GPIO.input(DOOR_SENSOR_PIN)
    # only play sound if door opens
    if (isOpen != oldIsOpen and isOpen):
        print('Change detected: play sound')
        id = randint(0, NUMBER_OF_AUDIO_FILES - 1)
        play_sound(f'{DIR}/audio/sigh_{id}.mp3')

    else:
        time.sleep(0.5)
