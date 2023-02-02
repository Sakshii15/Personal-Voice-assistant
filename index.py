import subprocess
import wolframalpha
import vlc
import pyttsx3
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import python_weather
import asyncio
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
from datetime import date
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning  !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon  !")

    else:
        speak("Good Evening !")

    assname = ("Siri 1 point o")
    speak("I am your Assistant")
    speak(assname)

def weather(city):
	city = city.replace(" ", "+")
	res = requests.get(
		f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
	print("Searching...\n")
	soup = BeautifulSoup(res.text, 'html.parser')
	location = soup.select('#wob_loc')[0].getText().strip()
	time = soup.select('#wob_dts')[0].getText().strip()
	info = soup.select('#wob_dc')[0].getText().strip()
	weather = soup.select('#wob_tm')[0].getText().strip()
	print(location)
	print(time)
	print(info)
	print(weather+"°C")


def username():
    speak("What should i call you")
    uname = takeCommand()
    speak("Welcome")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################")
    print("Welcome", uname)
    print("#####################")

    speak("How can i Help you")


def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query


if __name__ == '__main__':
    def clear(): return os.system('cls')

    clear()
    wishMe()
    username()

    while True:
        query = takeCommand().lower()

       
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query,sentences=5 )
            speak("According to Wikipedia")
            print(result)
            speak(result)  

        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("https://www.google.com/")

        elif 'open stack overflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query or "play song" in query:
            p = vlc.MediaPlayer(
                "C:\\Users\\JMD\\Desktop\\voice assisstant\\vs\\Khuda Bhi 128 Kbps.mp3")
            p.play()

            speak("do you want to stop the music?")
            query = takeCommand().lower()
            if 'stop' in query or 'yes' in query:
                p.stop()
            else:
                p.play()

        elif 'the time' in query or 'what is the time?' in query:
            today = date.today()
            print("Today's date:", today)

    

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you?")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that you are fine")

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query

        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak("siri 1 point o")
            print("My friends call me siri 1 point o")

        elif 'exit' in query or "shut down" in query:
            speak("Thanks for giving me your time")
            exit()

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Sakshi.")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif "calculate" in query:
            speak("Your speech recognition version is: "+sr.__version__)
            r = sr.Recognizer()
            my_mic_device = sr.Microphone(device_index=1)
            speak("Say what you want to calculate, example: 3 plus 3")
            while True:
                with my_mic_device as source:
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                    my_string = r.recognize_google(audio)
                    print(my_string)
                if my_string == "stop" or my_string == "exit":
                    speak("what else do u want to do?")
                    takeCommand()

                def get_operator_fn(op):
                    return {
                        '+': operator.add,
                        '-': operator.sub,
                        'x': operator.mul,
                        'divided': operator.__truediv__,
                        'Mod': operator.mod,
                        'mod': operator.mod,
                        '^': operator.xor,
                    }[op]

                def eval_binary_expr(op1, oper, op2):
                    op1, op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)
                print(eval_binary_expr(*(my_string.split())))
                speak("what else do u want to calculate")
                takeCommand()
        
        elif 'search' in query or 'play' in query:

            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif "who i am" in query:
            speak("If you talk then definitely your human.")

        elif "why you came to world" in query:
            speak("Thanks to sakshi. further It's a secret")

        elif 'powerpoint presentation' in query or "open powerpoint" in query:
            speak("opening Power Point presentation")
            power = r"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office PowerPoint 2007.lnk"
            os.startfile(power)

        elif 'love is' in query:
            speak("It is 7th sense that destroy all other senses")

        elif "who are you" in query:
            speak("I am your virtual assistant created by sakshi")

        elif 'reason for you' in query:
            speak("I was created as a Minor project by Miss Sakshi ")

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                       0,
                                                       "Location of wallpaper",
                                                       0)
            speak("Background changed successfully")

        elif 'open bluestack' in query:
            speak("opening Bluestacks")
            appli = r"https://www.bluestacks.com/"
            os.startfile(appli)

        elif 'news' in query or "news update" in query:

            try:
                jsonObj = urlopen(
                    "https://newsapi.org//v2//everything?q=tesla&from=2022-10-16&sortBy=publishedAt&apiKey=7a13b5c90af44f9fb121f49de7776e9c")
                data = json.load(jsonObj)
                i = 1

                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============''' + '\n')
                for item in data['articles']:

                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1

            except Exception as e:

                print(str(e))

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop siri from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open(
                "https://www.google.nl / maps / place/" + location + "")

        elif "camera" in query or "take a photo" in query:
            speak("Say cheeseeee!!")
            ec.capture(0, "siri Camera ", "img.jpg")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should i write")
            note = takeCommand()
            file = open('siri.txt', 'w')
            speak("Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = str(date.today())
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
                speak("notes updated")
            else:
                file.write(note)
                speak("notes updated")

        elif "show note" in query or "open notes" in query:
            speak("Showing Notes")
            file = open("siri.txt", "r")
            print(file.read())
            speak(file.read(6))

        # NPPR9-FWDCX-D2C8J-H872K-2YT43
        elif "siri" in query:

            wishMe()
            speak("siri 1 point o in your service Mister")
            speak(assname)

        elif "weather" in query or "weather report" in query:
            speak("Enter the Name of City")
            city = input("Enter the Name of City -> ")
            city = city+" weather"
            weather(city)
            print("Have a Nice Day:)")
            

        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")

        elif "Good Morning" in query:
            speak("A warm" + query)
            speak("How are you ?")
            speak(assname)

        # most asked question from google Assistant
        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")

        elif "how are you" in query:
            speak("I'm fine, glad you me that")

        elif "i love you" in query:
            speak("It's hard to understand")


        elif "do something siri" in query:
            speak("what should i do")
            takeCommand()







