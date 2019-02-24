import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    #print("Speak Anything:")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print("You said: {}".format(text))
