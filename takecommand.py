import speech_recognition as sr


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        r.energy_threshold = 3000
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        query = query.lower()
        # print("user said : ", query)
        return query
    except Exception as a:
        print(a)
