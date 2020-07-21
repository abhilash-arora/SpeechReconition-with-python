import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime
r=sr.Recognizer() #actually responsible for speech speech_recognition
def alexa_speak(audio_string):
    tts=gTTS(audio_string,lang='en')
    r=random.randint(1,10000000)
    audio_file='audio-'+str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
def record_audio(ask=False):
    with sr.Microphone() as source: #our source will be the microphone,we can use audio files too
        if ask:
            print(ask)
        #alexa_speak('Say something')
        #task1:To get the audio in a variable here voice_data and print the data
        audio=r.listen(source)
        voice_data=''
        #putting this in try and except block so that noices and echoes are not recognized and when the service is down
        try:
            voice_data=r.recognize_google(audio) #this is the google API used for the speech speech_recognition

        except sr.UnknownValueError:
            alexa_speak('Sorry,I did not get that')
        except sr.RequestError:
            alexa_speak('Sorry,my speech service is down')
        return voice_data
def respond(voice_data):
    if 'what is your name' in voice_data:
        alexa_speak('My name is Alexa')
    if 'what time is it' in voice_data:
        alexa_speak(ctime())
    if 'search' in voice_data:
        search=record_audio('What do you want to search for?')
        url='https://google.com/search?q=0'+search
        webbrowser.get().open(url)
        alexa_speak('Here is what I found for'+search)
    if 'find location' in voice_data:
        location=record_audio('What is the location?')
        url='https://google.nl/maps/place/'+ location +'/&amp;'
        webbrowser.get().open(url)
        alexa_speak('Here is the location for'+location)
    if 'exit' in voice_data:
        exit()
time.sleep(1)
alexa_speak('How can I help you?')
while 1:
    voice_data=record_audio()
    respond(voice_data)
