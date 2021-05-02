import pyttsx3

engine = pyttsx3.init()

rate = engine.getProperty('rate')
voices = engine.getProperty("voices")

engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 160)


def chatSpeech(text):
    engine.say(text)
    engine.runAndWait()
