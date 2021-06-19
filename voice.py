import os
import webbrowser as ws
import pyttsx3 as ps
import pywhatkit as pwk
import speech_recognition as sr
import sys

keeplistening = False
hear = sr.Recognizer()

engine = ps.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def search(Nman):                                       #module for searching in wiki
    ws.open(f'https://en.wikipedia.org/wiki/{Nman}', 2)


def listener():
    try:
        with sr.Microphone(device_index=1) as source:

            print("listening...")
            voice = hear.listen(source)
            command = hear.recognize_google(voice)
            command = command.casefold()
            if command == "shutdown the computer":  #this will shutdown the computer
                os.system("shutdown /s /t 1")
            elif command == "restart the computer": #this will restart the computer
                os.system("shutdown /r /t 1")
            elif "play" in command:    # this will play video on youtube
                song = command.replace('play', '')
                print('playing' + song)
                talk('playing' + song)
                pwk.playonyt(song)
            elif "search" in command: #this will search thing or person in wiki
                print(command)
                Nman = command.replace('search', '')
                talk('searching' + Nman)
                search(Nman)
            elif command == "who are you":
                tell = "i am your assistance"
                talk(tell)
            elif "fifa" in command:  #i used to this open game with voice commands
                talk("opening fifa")
                print("opening fifa")
                os.startfile("D:\games\FIFA 19\FIFA19.exe") #this is game path in my pc copy and paste the path which game you want to open
            elif "wwe" in command:
                talk("opening wwe")
                print("opening wwe")
                os.startfile("D:\games\WWE 2K19 v1.02\WWE2K19_x64.exe")
            elif "exit" in command:
                sys.exit()
            elif command == "i feel like crying":
                os.startfile("M:\songs\Billie_Eilish_-_lovely_(Lyrics)_ft._Khalid.mp3")

    except:
        pass


name = "hey what's up"
talk(name)
while (not keeplistening):
    listener()
