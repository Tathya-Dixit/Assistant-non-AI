from speak import speak
from processor import wishme
from takecommand import takecommand
from datafile import askme
from processor import wishme


def call():
    if 1:
        speak("hi sir, there for you always")
        wishme()
        while True:
            a = takecommand()
            askme(a)
    else:
        call()