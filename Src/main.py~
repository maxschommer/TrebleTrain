
import RPi.GPIO as GPIO
#!/usr/bin/python
import sys
import pygame as pg
import os
import time

pinInList = [16, 20, 12, 23, 5, 24, 22, 6, 25, 13]
pinSwitch= 4
#pinOutList=  [12, 13, 16] 
pinSounds = {pinInList[0] : '../SoundFiles/16thNotes.mp3', \
								pinInList[1] : '../SoundFiles/Triplet.mp3', \
								pinInList[2] : '../SoundFiles/Two8thNotes.mp3', \
								pinInList[3]: '../SoundFiles/WholeNote.mp3', \
								pinInList[4] : '../SoundFiles/HalfNote.mp3', \
								pinInList[5] : '../SoundFiles/QuarterNote.mp3', \
							   pinInList[6]: '../SoundFiles/One8thNote.mp3', \
								pinInList[7] : '../SoundFiles/HalfRest.mp3', \
								pinInList[8] : '../SoundFiles/WholeRest.mp3', \
								pinInList[9] : '../SoundFiles/QuarterRest.mp3', }
								
pinSoundsTeach = {pinInList[0] : '../SoundFiles/16thNotesName.mp3', \
								pinInList[1] : '../SoundFiles/TripletName.mp3', \
								pinInList[2] : '../SoundFiles/Two8thNotesName.mp3', \
								pinInList[3] : '../SoundFiles/WholeNoteName.mp3', \
								pinInList[4] : '../SoundFiles/HalfNoteName.mp3', \
								pinInList[5] : '../SoundFiles/QuarterNoteName.mp3', \
								pinInList[6] : '../SoundFiles/One8thNoteName.mp3', \
								pinInList[7] : '../SoundFiles/HalfRestName.mp3', \
								pinInList[8] : '../SoundFiles/WholeRestName.mp3', \
								pinInList[9] : '../SoundFiles/QuarterRestName.mp3', }
								
#Audio Initialization
freq = 44100    # audio CD quality
bitsize = -16   # unsigned 16 bit
channels = 2    # 1 is mono, 2 is stereo
buffer = 2048   # number of samples (experiment to get right sound)
pg.mixer.init(freq, bitsize, channels, buffer)
pg.mixer.music.set_volume(1)
GPIO.setmode(GPIO.BCM)

for pinIn in pinInList:
	GPIO.setup(pinIn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	print(GPIO.input(pinIn))
GPIO.setup(pinSwitch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#for pinOut in pinOutList:
#	GPIO.setup(pinOut, GPIO.OUT, initial=GPIO.LOW)

def btn_callback(pinIn):
#	if GPIO.input(pinIn):
	print(pinIn)
	print(1)
		#GPIO.output(25, 1)
#		play_music('../SoundFiles/QuarterNote.mp3')
#		GPIO.output(25, 0)


                 
#for pinIn in pinInList:
#	GPIO.add_event_detect(pinIn, GPIO.BOTH, callback=lambda x: btn_callback(pinIn))



def play_music(music_file):
    '''
    stream music with mixer.music module in blocking manner
    this will stream the sound from disk while playing
    '''
    clock = pg.time.Clock()
    try:
        pg.mixer.music.load(music_file)
        print("Music file {} loaded!".format(music_file))
    except pg.error:
        print("File {} not found! {}".format(music_file, pg.get_error()))
        return
 
    pg.mixer.music.play()
    
    # If you want to fade in the audio...
    # for x in range(0,100):
    #     pg.mixer.music.set_volume(float(x)/100.0)
    #     time.sleep(.0075)
    # # check if playback has finished
    while pg.mixer.music.get_busy():
        clock.tick(30)
 
 

try:
	while True:
		soundsToPlay = pinSounds
		if GPIO.input(pinSwitch):
			soundsToPlay = pinSoundsTeach
			
		for pinIn in pinInList:
			if GPIO.input(pinIn):
				print(pinIn)
				play_music(soundsToPlay[pinIn])
				time.sleep(.2)
		
except KeyboardInterrupt:
	GPIO.cleanup()
	pg.mixer.music.fadeout(1000)
	pg.mixer.music.stop()
	raise SystemExit
	print('Interupted: Exiting')
