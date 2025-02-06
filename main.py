import re
import speech_recognition as sr
import webbrowser
import pyttsx3

import google.generativeai as genai
import os
# import requests
from songfile import music



 

recognizer=sr.Recognizer()
engine= pyttsx3.init()


genai.configure(api_key=os.environ["api_key"])

model = genai.GenerativeModel('gemini-1.5-flash')



def speak(text):
    clean_text=re.sub(r'[^\w\s]', '', text)
    engine.say(clean_text)
    engine.runAndWait()

def processcommand(c):

    try:
        if "open google" in c.lower():
            webbrowser.open("https://google.com")
        elif "open youtube" in c.lower():
            webbrowser.open("https://youtube.com") 

        elif c.lower().endswith("song"):
            song = c.lower().split(" ")[1]
            song: str=song
            if song in music:
                speak(f"now playing {song}")
                webbrowser.open(music[song])
            else:
                speak(f"sorry , i coudent find this {song} song")    


        elif "stop" in c.lower():
            speak("stoping sir")       
            exit()
        else:
            response = model.generate_content(c)
            speak(response.text)
            print(response.text)
    except Exception as e:
        print(f"error:{e}")        
        

 

if __name__=="__main__":
    speak("initilizing friday...")
    while True:
        #it showld lesten word "jarvis"
        #the below code is used for obtaining audio from microphone
        r=sr.Recognizer()

    #the below code is for recognize speech using sphinx
        try:
            with sr.Microphone() as source:
                print("lestning....")
                recognizer.adjust_for_ambient_noise(source)
                audio= recognizer.listen(source , timeout=2)
            command = recognizer.recognize_google(audio) 
            print("you said : ", command )

            if "friday" in command.lower():
                speak("yes  how can i help you")
                print("yes how can i help you")
                #lesten for comand 
                with sr.Microphone() as source:
                    print("lestening for comand...")
                    recognizer.adjust_for_ambient_noise(source)
                    audio = recognizer.listen(source, timeout=5)

                command=recognizer.recognize_google(audio)
                print(command)

                processcommand(command )
        except Exception as e:
            print("error;{}".format(e))    
