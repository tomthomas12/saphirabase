import random
import datetime
import webbrowser
import pyttsx3
import wikipedia
from pygame import mixer
import speech_recognition as sr
from speech_recognition.__main__ import r, audio

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
volume = engine.getProperty('volume')
engine.setProperty('volume', 10.0)
rate = engine.getProperty('rate')

engine.setProperty('rate', rate - 25)

greetings = ['saphira','hey there', 'hello', 'hi', 'Hai', 'hey!', 'hey']
question = ['How are you?', 'How are you doing?']
responses = ['Okay', "I'm fine"]
var1 = ['who made you', 'who created you','what are you']
var2 = ['I_am_Saphira_I_was_created_by_Tom_Thomas_right_in_his_computer.', 'Tom_thomas', 'Tom_Some_guy_whom_i_never_got_to_know.']
var3 = ['what time is it', 'what is the time', 'time']
var4 = ['who are you', 'what is you name']
var5 = ['I_am_Saphira', 'I_was_created_by_Tom_Thomas_right_in_his_computer']
cmd1 = ['open browser', 'open google']
cmd2 = ['play music', 'play songs', 'play a song', 'open music player', 'sing a song']
cmd4 = ['open YouTube', 'i want to watch a video']
cmd5 = ['tell me the weather', 'weather', 'what about the weather']
cmd6 = ['exit', 'close', 'goodbye', 'nothing']
cmd7 = ['what is your color', 'what is your colour', 'your color', 'your color?']
colrep = ['Right now its rainbow', 'Right now its transparent', 'Right now its non chromatic']
cmd8 = ['what is you favourite colour', 'what is your favourite color']
cmd9 = ['thank you']


repfr9 = ['youre welcome', 'glad i could help you']

while True:
    now = datetime.datetime.now()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tell me something:")
        audio = r.listen(source)
        try:
            print("You said:- " + r.recognize_google(audio))
        except sr.UnknownValueError:
            print("Could not understand audio")
            engine.say('I didnt get that. Rerun the code')
            engine.runAndWait()
    if r.recognize_google(audio) in greetings:
        random_greeting = random.choice(greetings)
        print(random_greeting)
        engine.say(random_greeting)
        engine.runAndWait()
    elif r.recognize_google(audio) in question:
        engine.say('I am fine')
        engine.runAndWait()
        print('I am fine')
    elif r.recognize_google(audio) in var1:
        engine.say('I was made my Tom Thomas , also known as black angel')
        engine.runAndWait()
        reply = random.choice(var2)
        print(reply)
    elif r.recognize_google(audio) in cmd9:
        print(random.choice(repfr9))
        engine.say(random.choice(repfr9))
        engine.runAndWait()
    elif r.recognize_google(audio) in cmd7:
        print(random.choice(colrep))
        engine.say(random.choice(colrep))
        engine.runAndWait()
        print('It keeps changing every micro second')
        engine.say('It keeps changing every micro second')
        engine.runAndWait()
    elif r.recognize_google(audio) in cmd8:
        print(random.choice(colrep))
        engine.say(random.choice(colrep))
        engine.runAndWait()
        print('It keeps changing every micro second')
        engine.say('It keeps changing every micro second')
        engine.runAndWait()
    elif r.recognize_google(audio) in cmd2:
        mixer.init()
        mixer.music.load("song.wav")
        mixer.music.play()
    elif r.recognize_google(audio) in var4:
        engine.say('I am Saphira , I am a personal assistant made my Tom Thomas , also known as black angel , he made me to help people like you so how can i help you')
        engine.runAndWait()
    elif r.recognize_google(audio) in cmd4:
        engine.say("opening Youtube")
        engine.runAndWait()
        webbrowser.open('www.youtube.com')
    elif r.recognize_google(audio) in cmd6:
        print('see you later')
        engine.say('see you later')
        engine.runAndWait()
        exit()
    elif r.recognize_google(audio) in cmd5:
        owm = pyowm.OWM('YOUR_API_KEY')
        observation = owm.weather_at_place('Pala, IN')
        observation_list = owm.weather_around_coords(9.708380, 76.684914)
        w = observation.get_weather()
        w.get_wind()
        w.get_humidity()
        w.get_temperature('celsius')
        print(w)
        print(w.get_wind())
        print(w.get_humidity())
        print(w.get_temperature('celsius'))
        engine.say(w.get_wind())
        engine.runAndWait()
        engine.say('humidity')
        engine.runAndWait()
        engine.say(w.get_humidity())
        engine.runAndWait()
        engine.say('temperature')
        engine.runAndWait()
        engine.say(w.get_temperature('celsius'))
        engine.runAndWait()
    elif r.recognize_google(audio) in var3:

        print("Current date and time : ")
        print(now.strftime("The time is %H:%M"))
        engine.say(now.strftime("The time is %H:%M"))
        engine.runAndWait()
    elif r.recognize_google(audio) in cmd1:
        engine.say("opening google")
        engine.runAndWait()
        webbrowser.open('www.google.com')
   
    else:
        engine.say("please wait")
        engine.runAndWait()
        print(wikipedia.summary(r.recognize_google(audio)))
        engine.say(wikipedia.summary(r.recognize_google(audio)))
        engine.runAndWait()
        userInput3 = input("or else search in google")
        webbrowser.open_new('www.google.com/search?q=' + userInput3)
