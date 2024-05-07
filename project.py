import pyttsx3   #Text to Speech
import speech_recognition as sr  
import datetime 
import wikipedia  #Retrive information from Wikipedia
import webbrowser #interacted with web browsers
import smtplib #use to send mail
import bs4
import pyjokes
import time
import operator
import subprocess
import keyboard
import wolframalpha
import os #opening applications
import winshell #interacted with windows 



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe(): #wish user base current time 
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Hello, Good Morning!, Please tell me how may I help you")

    elif hour>=12 and hour<18:
        speak("Hello, Good Afternoon!, Please tell me how may I help you")   

    else:
        speak("Hello, Good Evening!, Please tell me how may I help you")  

def date():
            now = datetime.datetime.now()
            month_name = now.month
            day_name = now.day
            month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
            ordinalnames = [ '1st', '2nd', '3rd', ' 4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd','24rd', '25th', '26th', '27th', '28th', '29th', '30th', '31st'] 

            speak("Today is "+ month_names[month_name-1] +" " + ordinalnames[day_name-1] + '.')

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('manshipatel131415@gmail.com', 'password')
    server.sendmail('manshipatel131415@gmail.com', to, content)
    server.close()

def note(text): #create a note files
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"

    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])

if __name__ == "__main__":
    wishMe()
    while True:

        query = takeCommand().lower()
        app_string = ["open word", "open powerpoint", "open excel", "open zoom","open notepad",  "open chrome"]
        app_link = [r'\Word.lnk',r'\PowerPoint.lnk', r'\Excel.lnk', r'\Zoom.lnk', r'\Notepad.lnk', r'\Google Chrome.lnk' ]
        app_dest = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs'

        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)

            if app_string[0] in query:
                os.startfile(app_dest + app_link[0])

                speak("Microsoft office Word is opening now")

            if app_string[1] in query:
                os.startfile(app_dest + app_link[1])
                speak("Microsoft office PowerPoint is opening now")

            if app_string[2] in query:
                os.startfile(app_dest + app_link[2])
                speak("Microsoft office Excel is opening now")
        
            if app_string[3] in query:

                os.startfile(app_dest + app_link[3])
                speak("Zoom is opening now")


            if app_string[4] in query:
                os.startfile(app_dest + app_link[4])
                speak("Notepad is opening now")
        
            if app_string[5] in query:
                os.startfile(app_dest + app_link[5])
                speak("Google chrome is opening now")
                       

            if 'news' in query:
                news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/city/mangalore")
                speak('Here are some headlines from the Times of India, Happy reading')
                time.sleep(6)

            if 'cricket' in query:
                news = webbrowser.open_new_tab("cricbuzz.com")
                speak('This is live news from cricbuzz')
                time.sleep(6)

            if 'corona' in query:
                news = webbrowser.open_new_tab("https://www.worldometers.info/coronavirus/")
                speak('Here are the latest covid-19 numbers')
                time.sleep(6)

            if 'time' in query:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"the time is {strTime}")

            if 'date' in query:
                date()
            
            if 'make a note' in query:
                statement = statement.replace("make a note", "")
                note(statement)


             

            speak(results)        

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
        
        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
                 
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
        
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/"+location+"")

        
        elif 'search' in query or 'play' in query:
             
            query = query.replace("search", "")
            query = query.replace("play", "")         
            webbrowser.open(query)

        elif 'email to manshi' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "manshipatel131415@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sir i am not able to send this email")