import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')     #voicec change line one
engine.setProperty('voice', voices[1].id)     #voice change line two    '1= female voice / 0= male voice'
engine.say("Hello, I'm Alexa.")
engine.say('How can I help you?')
engine.runAndWait()

try:
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'alexa' in command:
            print(command)

except:
    pass