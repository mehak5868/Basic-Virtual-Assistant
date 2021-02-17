import pyttsx3 as tts
import speech_recognition as sr
import os
import webbrowser
import datetime
import wikipedia
from datetime import date
import smtplib
import requests
#from ecapture import ecapture as ec
import random

print("Initialising Robo...")
engine = tts.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    wish ="I am Robo.How may I help you ?"
    if hour >=0 and hour<12:
        speak("Good Morning"+wish)
        print("Robo : Good Morning,",wish)
    elif hour >=12 and hour <18:
        speak("Good Afternoon,"+wish)
        print("Robo : Good Afternoon,",wish)
    else :
        speak("Good Evening,"+wish)
        print("Robo : Good Evening,",wish)
wishMe()

#this function take command from microphone
def takeCoomand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        audio = r.listen(source)
    try :
        print("Recognizing.....")
        query = r.recognize_google(audio,language='en-in')
        print(f"user :{query}\n")
    except Exception  :
        print("Say That again please")
    return query
#speak("Hello, I am Robo.How may I help you ?")
#takeCoomand()


def DateTime(query):
    now = datetime.datetime.now()
    if 'time' in query:
        print("Robo :",now.hour,":",now.minute)
        speak('Current time is %d hours %d minutes' %(now.hour,now.minute))
    if 'date' in query:
        now = date.today()
        d1 = now.strftime("%d/%m/%Y")
        print("Robo :",d1)
        
        
def wiki(query) :
    try:
        print('Robo : Searching wikipedia.....')
        speak('Searching wikipedia.....')
    
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    except wikipedia.exceptions.DisambiguationError as e:
        s = random.choice(e.options)
        print(s)
        speak(s)
    except wikipedia.exceptions.WikipediaException as e:
        print('Search not include, try again wikipedia and your search')
    
    
    
    
    
#print("User : Wikipedia what is whatsapp messenger")
#wiki("what is whatsapp messenger according to wikipedia")


def openYoutube():
    print("Robo : Opening...")
    speak("Opening...")
    url = "youtube.com"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
    
    
#print("User : Open You Tube ")
#openYoutube()


def playsong():
    print("Robo : Playing Music.... ")
    speak("Playing music")
    song_dir = "C:\\Users\\dell\\Music\\songs"
    songs = os.listdir(song_dir)
    print(songs)
    os.startfile(os.path.join(song_dir,songs[0]))

def search(query):
    url = "https://google.com/search?q=" + query
    webbrowser.get().open(url)
    print('Robo : Here is what I found')
    speak('Here is what I found')

def map(query):
    url = "http://google.nl/maps/place"+query+'/&amp;'
    webbrowser.get().open(url)
    print('Robo : Here is ' + query)
    speak("Here is the result :")
    
def sendEmail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    emailId=input("Enter Email Id :")
    password=input("Enter password:")
    if emailId.__contains__("@") and emailId.__contains__(".com"):
        server.login(emailId,password)
        print("Successfully login")
        print("Robo:To whom??")
        speak("To whom :")
        to=input("Enter mail id :")
        #to=takeCoomand()
        try:
            print("Robo : What should I send ??? ")
            speak("What should  I send ")
            #content=takeCoomand()
            content =  input("Enter a content : ")
            server.sendmail(emailId,to,content)
            print("Robo : Email has been sent successfully")
            speak("Email has been sent successfully")
        except Exception as e :
            print(e)
            speak("Sorry,I am not able to send this email")
    else :
        print("Robo:Enter a valid email id")
        speak("Enter a valid email id ")
        sendEmail()
        
        
def openGoogle():
    print("Robo:Opening Google...")
    speak("Opening google")
    webbrowser.open("google.com")
    
def _extract_temp(weatherdata):
    temp = weatherdata['main']['temp']
    return temp


def _extract_desc( weatherdata):
    return weatherdata['weather'][0]['description']

def weather():
    
    speak("Robo:Location")
    print("Robo :Enter a loaction")
    #city_name = takeCoomand()
    city_name = input()
    api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&units=metric";
    api_key = "0fd8fe4f2c477a8778a86a1a328ddfc0"
    r=requests.get(api_url.format(city_name,api_key))
    weather_data = (r.json())
    temp = _extract_temp(weather_data)
    description = _extract_desc(weather_data)
    print("Currently, in {}, its {} degrees with {}".format(city_name, temp, description))
    speak( "Currently, in {}, its {} degrees with {}".format(city_name, temp, description))
#def camera ():
 #   ec.capture(0,"robo camera","img.jpg")
  #  print("Robo: Here is your picture ")
   # speak("Here is your picture ")

def news():
    webbrowser.open_new_tab("https://edition.cnn.com/")
    print('Robo: Here are some headlines from the CNN,Happy reading')
    speak('Here are some headlines from the CNN,Happy reading')



def takecommand():
    #send query = takeCoomand()
    query = input("User:")
    print(query)
    query= query.lower()
    if 'time' or 'date' in query:
        DateTime(query)
    if 'wikipedia' in query :
        wiki(query)
    if 'open youtube' in query:
        openYoutube()
    if 'play music' in  query:
        playsong()
    if 'search' in query :
        search(query)
    if 'location' in query :
        map(query)
    if 'send mail' in query :
        sendEmail()
    if 'open google' in query:
        openGoogle()
    if 'weather' in  query:
        weather()
    #if 'take a picture' in query or 'take a phone' in query :
        #camera()
    if 'news' in query :
        news()
    if 'bye' in query or  'goodbye' in query:
        print('Robo: Your virtual assistant Robo is shutting down,Good bye')
        speak('your virtual assistant Robo is shutting down,Good bye')
        
while True :
    takecommand()

