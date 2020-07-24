"""
Function holds the data and function which i will use to run app.py
"""
import pyttsx3
import speech_recognition as sr
import wikipedia # this will help you to search wikipedia...
import datetime
import smtplib
from email.message import EmailMessage
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # to set the voice
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)  # i set here the men's voice 1 is for women in my PC


def speak(audio):
    """
    This function takes a string as a input and gives audio as output
    """
    engine.say(audio)  # will say the object i passed
    engine.runAndWait()


def input_command():
    """
    This function takes audio and using function like Recognizer and recognize google convert audio to string.
    """
    listen = sr.Recognizer()
    with sr.Microphone() as source:
        print("I m hearing...")
        listen.pause_threshold =1 # now it will w8 for 1s to listen
        audio = listen.listen(source)
    try:
        print("Recognizing...")
        query = listen.recognize_google(audio,language='en-in')
        print(f"You said: {query}")
        return query

    except Exception :
        print("Please say that again")
        return "None"
    
def search_wikipedia(command):
    """
    This command is for searching wikipedia as a content writter i need to read wikipedia frequently.
    Function isn't complete yet.
    """
    try:
        speak("searching wikipedia...")
        command = command.replace("wikipedia"," ") #removing wikipedia from the user command
        command = command.replace("search"," ") #removing wikipedia from the user command
        result = wikipedia.summary(command,sentences = 4)
        print(result)
        speak("As per search from wikipedia...")
        speak(result) 
    except Exception:
        pass


class AI:

    """
    This class is basically encapsulation
    """

    def __init__(self, name):
        self.name = name


    def wish_me(self):
        """
        to wish user and introduction
        """
        hr = int(datetime.datetime.now().hour)

        if 0 <= hr < 12:
            speak(f"Good Morning {self.name}")
        elif 12 <= hr < 18:
            speak(f"Good Afternoon {self.name}")
        else:
            speak(f"Good evening {self.name}")

        speak("I'm Heisenberg how can i help you")

    def send_mail(self):
        """
        Function as user to write his/her email id and password and recipient email.
        Subject and body is taken as audio command.
        smtplib is the library used for this function
        """
        speak(f"{self.name} type your email id")
        email_my = input()
        speak(f"{self.name} type your password")
        password = input()
        speak(f"{self.name} type recipient's email id")
        email_recipient = input()
        speak(f"{self.name}, What is the subject of email")
        sub = input_command().title()

        speak(f"{self.name} what should i send?")
        body = input_command()
        server = smtplib.SMTP(host='smtp.gmail.com',port=587)
        server.ehlo()
        server.starttls()
        server.login(email_my,password)
        email = EmailMessage()
        email['subject'] = sub
        email['From'] = email_my
        email['To'] = email_recipient
        email.set_content(body)
        server.send_message(email)
        server.quit()
        return
