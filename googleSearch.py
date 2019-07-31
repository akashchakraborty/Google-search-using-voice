import sys
from googlesearch import search 
import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def takeCommand():
	# It takes microphone input from user and returns string output
	r = sr.Recognizer()
	with sr.Microphone() as source :
		print("Listening... ")
		#r.pause_threshold = 0.8
		audio = r.listen(source)
	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language='en-in')
		print(f"User Said: {query}\n")

	except Exception as e:
		print(e)
		print("Say That Again Please...")
		return "None"
	return query

def greet():
    
    speak("Hey  There...       What is your name?")
    name = takeCommand().lower()
    speak("Hi " + name + " I    am    your   personal   search   engine   powered   by   google")

def searching():
    speak("So... What is it you want to look up in the internet ... other than pornograhy?")
    query = takeCommand()
    for j in search(query, tld="com", num=15, stop=10, pause=3): 
        print(j) 

def exitormore():
    speak("You want to look up for something more... or exit?")
    command = takeCommand().lower()
    if command == "exit":
        speak("OK! Bye it was nice meeting you!")
        sys.exit()
    elif command == "more":
        searching()





greet()
searching()
exitormore()
