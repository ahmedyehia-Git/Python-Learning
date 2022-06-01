# this code to convert text to audio
# pyttsx3 could not be install well, try pip and pip3 for pyttsx3 2.9 & 2.7
# after install 2.7 it give no output but there is no error 
# save_to_file is not working as well

import pyttsx3


vo = pyttsx3.init('dummy') # tis is to initiate the package 

vo.setProperty('rate', 100) # this to set the speed of speech 
vo.setProperty('volume', 1.1) # to adjust the volume, 1 same volume as set b computer

voices = vo.getProperty('voices') # make variable to save the different voices in the package
vo.setProperty('voice', voices[1].id) # [0] for male voice, [1] for female voice,.id is a must

vo.say('Hello World')

#vo.save_to_file('Hello World', 'test.mp3') # this is not working

vo.runAndWait()