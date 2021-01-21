import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id) # for female voice voices[1].id


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print(audio)
    
