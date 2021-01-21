import sqlite3
from processor import process
from speak import speak
from takecommand import takecommand


def askme(command):
    conn = sqlite3.connect("assistant.db")
    c = conn.cursor()
    try:
        a = c.execute(f"SELECT reply from command_reply WHERE command like '{command}'")
        b = a.fetchall()
        d = []
        for i in str(b):
            d.append(str(i))
        for i in range(0, 4):
            d.pop()
        e = ""
        for i in range(3, len(d)):
            e = e+str(d[i])
        process(e)
    except IndexError:
        speak("sorry sir, i couldn't understand that")
        speak("do you want me to save this?")
        ans = takecommand()
        if ans == "yes":
            speak("ok, sir! please tell me the reply of this command")
            reply = takecommand()
            c.execute(f"insert into command_reply values('{command}','{reply}')")
            speak("saved it sir")
        elif ans == "no":
            speak("ok, sir")
    conn.commit()
    c.close()
    conn.close()

