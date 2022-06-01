# this code to transfer audio to text
# need to install speechrecog, pip3 install speechrecog
# install pyaido to recognize microphone audio, installation as following 
# sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
# sudo apt-get install ffmpeg libav-tools
# sudo pip install pyaudio

import speech_recognition
import pyaudio 

rec = speech_recognition.Recognizer() # we initiating the package and save it in variable

while True: # to make program run again and again
    with speech_recognition.Microphone() as sor: # we select the source of audio, as sor to give short name for it
        print("Please say something....")
        audio = rec.listen(sor) # ask code to listen

    text = (rec.recognize_google(audio)) # variable that save the recognized text
    # print(text) # if i need to print recognized text directly 
    if 'hello' in text: #
        print('hello')
    elif 'how are you' in text:
        print('fine thank you')
    else:
        print('could not understand you!')
        
# it is not working although there is no error, seems it is something related to hardware 
# to terminate the running code use ctrl+c