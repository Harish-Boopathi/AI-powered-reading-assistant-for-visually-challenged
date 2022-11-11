import pygame
import speech_recognition as sr  #pip install speechRecognition
from pygame import mixer
import pyttsx3     #pip install pyttsx3
import datetime
import wikipedia     #pip install wikipedia
import webbrowser
import os
import smtplib
import cv2
import pytesseract    # will convert the image to text string
import gtts  
from playsound import playsound
from PIL import Image
from googletrans import Translator
from gtts import gTTS     #Import Google Text to Speech
from IPython.display import Audio 
import RPi.GPIO as GPIO

def program():  #identifies the signal to start from user using switch  
    GPIO.setwarnings(False)
    GPIO .setmode(GPIO.BOARD)
    inPin = 15
    GPIO.setup(inPin,GPIO.IN)
    while True:
        x = GPIO.input(inPin)
        if x==1:
            return x 


engine = pyttsx3.init()  
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[2].id)  #selecting voices that are inbuild in pyttsx3
engine.setProperty('rate',168)              #adjusting the reading speed
engine.setProperty('volume', 2.0)           #adjusting volume
engine.runAndWait()

       
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():   #greets acording to time
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning buddy!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon buddy!")  

    else:
        speak("Good Evening buddy!")  

    speak("I am Jarvis how may I help you!")      

def takeCommand():
    r = sr.Recognizer()     #It takes microphone input from the user and returns string output
    with sr.Microphone() as mic:
        print("Listening...")
        speak("Listening...")
        r.adjust_for_ambient_noise(mic)
        audio = r.listen(mic)
    try:
        print("Recognizing...")
        speak("Recognizing...")
        query = r.recognize_google(audio, language='en_IN')  #languages can be adjusted according to accent
        print("you said",query)
        speak("you said")
        speak(query)
    except Exception:
        print("Say that again please...")
        speak("Say that again please...")
        return "None"
    return query



if __name__ == "__main__":
    x=program()
    if x==1:
        wishMe()
        while True:
    
    # if 1:
            query = takeCommand().lower()

        # Logic for executing tasks based on query
            if 'Hi' in query:
                speak('Hi buddy')
           
            elif 'photo' in query:
                videoCaptureObject = cv2.VideoCapture(0) #capturing image 
                result = True
                while(result):
                    ret,frame = videoCaptureObject.read()
                    cv2.imwrite("your_path/output.jpg",frame)   #saving image in jpg formate
                    result = False
                videoCaptureObject.release()
                cv2.destroyAllWindows()
                speak('photo taken')       #indicating user that the photo is saved
           
                if True :
               
                        img = Image.open("your_path/output.jpg")
               

                   # describes image format in the output
                        print(img)
                   # converts the image to result and saves it into result variable
                        result = pytesseract.image_to_string(img)       
                   # write text in a text file and save it to source path
                        with open('your_path/output.txt',mode ='w') as file:
                            file.write(result)

                        fh = open("your_path/output.txt", "r")
                        myText = fh.read().replace("\n", " ")
                        language = 'en'
                        try:
                            output = gTTS(text=myText, lang=language, slow=False) #converting text to audio
                            output.save("your_path/output.mp3")
                            fh.close()
                        except AssertionError:
                            speak("no text to read")        #indicating if there is no text in the image
                            continue

                        mixer.init()
                        mixer.music.load("your_patht/output.mp3")      #playing the audio file
                        mixer.music.set_volume(1.5)
                        mixer.music.play()

       
            elif 'play' in query:
                mixer.init()
                mixer.music.load("your_path/output.mp3")         
                mixer.music.set_volume(1.5)
                mixer.music.play()

            if 'audio' in query:
                mixer.init()
                mixer.music.load("your_path/output.mp3")         
                mixer.music.set_volume(1.5)
                mixer.music.play()

            if 'pass' in query:
                mixer.music.pause()
                
            elif 'pause' in query:
                mixer.music.pause()
                
            elif 'continue' in query:
                mixer.music.unpause()
                
            elif 'replay' in query:
                mixer.init()
                mixer.music.load("your_path/output.mp3")         
                mixer.music.set_volume(1.5)
                mixer.music.play()
                
            elif 'reply' in query:
                mixer.init()
                mixer.music.load("your_path/output.mp3")         
                mixer.music.set_volume(1.5)
                mixer.music.play()
                
            elif 'stop' in query:
             # Stop the mixer
                 mixer.music.stop()
              
            elif 'exit' in query:
                 break                   

