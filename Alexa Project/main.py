import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')     #voice change line one
engine.setProperty('voice', voices[1].id)     #voice change line two    '1= female voice / 0= male voice'

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'lisa' in command:
                command = command.replace('lisa', '')
                print(command)

    except:
        pass
    return command

def run_lisa():
    command = take_command()
    if  'goodbye lisa' in command:
        print("Goodbye my friend untill we meet again")
        sys.exit(run_lisa())

    #print(command)

    elif 'who are you' in command:
        print("My name is lisa. I'm internet assistant. I'm trying to make your work easily. Have you any proble with that?")
        talk("My name is lisa. I'm internet assistant. I'm trying to make your work easily. Have you any proble with that?")

    elif 'no dear' in command:
        talk("Ok then, what do you want from me actually?")
        print("Ok then, what do you want from me actually?")

    elif 'are you single' in command:
        talk("No dear, I'm actually relationship with internet.")

    elif 'give me a kiss' in command:
        talk("I'm little bit shy. But that's fine. umma")

    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time now' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk("Now timw is "+ time)

    elif 'how are you' in command:
        talk("I'm fine thanks for asking. How are you?")
        print("I'm fine thanks for asking. How are you?")

    elif 'fine too' in command:
        talk("Ok, dear")
        print("Ok, dear")

    elif 'joke' in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())

    elif 'who is ' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)



while True:
    run_lisa()