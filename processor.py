import datetime
import random
import os
import webbrowser
import wikipedia
from takecommand import takecommand
from speak import speak


def wishme():
    h = int(datetime.datetime.now().hour)
    if 0 <= h < 12:
        speak("good morning sir")
    elif 12 <= h <18:
        speak("good afternoon sir")
    else:
        speak("good evening sir")
time = datetime.datetime.now().strftime("%H:%M:%S")


def process(command):
    if command == "hello":
        a = ["hello, sir","hi,sir","hello","hi","yo! wassup"]
        b = random.randrange(0,7)
        c = str(a[b])
        speak(c)
    elif command == "exit":
        speak("ok sir! bye bye")
        exit(takecommand)
    elif command == "google":
         speak("ok! sir")
         webbrowser.open("google.com")
    elif command == "youtube":
         speak("ok! sir")
         webbrowser.open("youtube.com")
    elif command == "freeicon":
         speak("ok! sir")
         webbrowser.open("freeicons.io")
    elif command == "time":
         speak("Sir, the time is : "+time)
    elif command == "music":
        os.startfile("playlist path")
        speak("ok sir! here's your music enjoy!")
    elif command == 'search wikipedia':
        speak("what u want to search")
        search = takecommand()
        res = wikipedia.summary(search, sentences=3)
        speak("according to wikipedia : "+res)
    else:
         pass
