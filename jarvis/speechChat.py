import speech_recognition as sr

recogniser = sr.Recognizer()


def speechChat():
    with sr.Microphone() as source:
        recogniser.pause_threshold = 1
        recogniser.adjust_for_ambient_noise(source)
        text = recogniser.listen(source)
        try:
            recognised_text = recogniser.recognize_google(text)
        except:
            recognised_text = "Errors"
    return recognised_text
