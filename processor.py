import datetime
import random
import os
import webbrowser
import pyjokes
import pywhatkit
import wikipedia
from takecommand import takecommand
from speak import speak
import time


def wishme():
    h = int(datetime.datetime.now().hour)
    if 0 <= h < 12:
        speak("good morning sir")
    elif 12 <= h < 18:
        speak("good afternoon sir")
    else:
        speak("good evening sir")


currtime = datetime.datetime.now().strftime("%I %M:%p")
chrome = "path of your browser.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome))


def process(command):
    if command == "hello":
        a = ["hello, sir", "hi,sir", "hello", "hi", "yo! wassup"]
        b = random.randrange(0, 7)
        c = str(a[b])
        speak(c)

    elif command == "exit":
        speak("ok sir! bye bye")
        exit()

    elif command == "google":
        speak("ok! sir")
        webbrowser.get('chrome').open_new_tab("google.com")

    elif command == "youtube":
        speak("do you want me to open any specific video or want me to open youtube only")
        rep = takecommand()
        if "specific video" in rep:
            speak("what is the title of the video")
            video = takecommand()
            speak("ok sir! playing "+video+" on youtube")
            pywhatkit.playonyt(video)
        elif "open youtube" in rep:
            webbrowser.get('chrome').open_new_tab("www.youtube.com")

    elif command == "stack overflow":
        speak("ok! sir, opening stack overflow")
        webbrowser.get('chrome').open_new_tab("www.stackoverflow.com")

    elif command == "time":
        speak("Sir, the time is : "+currtime)

    elif command == "music":
        speak("which song do you want to be played")
        song = takecommand()
        pywhatkit.playonyt(song)
        speak("ok sir! here's your song enjoy!")

    elif command == 'search wikipedia':
        speak("what u want to search")
        search = takecommand()
        try:
            res = wikipedia.summary(search, sentences=3)
            speak("according to wikipedia "+res)
            time.sleep(1)
            speak("do you want to search more")
            ask = takecommand()
            if "yes" in ask:
                process("search wikipedia")
            elif "no" in ask:
                pass

        except:
            speak("could not found"+search)

    elif command == "sublime":
        os.startfile("path\\sublime_text.exe")
        speak("opening it sir")

    elif command == "joke":
        speak(pyjokes.get_joke("en"))
    else:
        pass
