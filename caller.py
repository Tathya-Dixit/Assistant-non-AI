from speak import speak
from takecommand import takecommand
from datafile import askme
from processor import wishme


def call():
    try:
        init = takecommand()
        if init == "alex":
            speak("hi sir, there for you always")
            wishme()
            while True:
                a = takecommand()
                askme(a)
        else:
            call()
    except Exception as a:
        print(a)
