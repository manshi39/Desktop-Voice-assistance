import pyttsx3   
import speech_recognition as sr  
import datetime 
import wikipedia  
import webbrowser 
import smtplib 
import subprocess
import os 
import winshell 
import pyautogui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe(): 
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Hello, Good Morning!, Please tell me how may I help you")

    elif 12 <= hour < 18:
        speak("Hello, Good Afternoon!, Please tell me how may I help you")   

    else:
        speak("Hello, Good Evening!, Please tell me how may I help you")  

def date():
    now = datetime.datetime.now()
    month_name = now.month
    day_name = now.day
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    ordinalnames = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24rd', '25th', '26th', '27th', '28th', '29th', '30th', '31st'] 

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

def note(text):
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

            for i, app in enumerate(app_string):
                if app in query:
                    os.startfile(app_dest + app_link[i])
                    speak(f"{app} is opening now")

            if 'news' in query:
                webbrowser.open_new_tab("https://timesofindia.indiatimes.com/city/mangalore")
                speak('Here are some headlines from the Times of India. Happy reading.')

            if 'cricket' in query:
                webbrowser.open_new_tab("cricbuzz.com")
                speak('This is live news from Cricbuzz.')

            if 'corona' in query:
                webbrowser.open_new_tab("https://www.worldometers.info/coronavirus/")
                speak('Here are the latest Covid-19 numbers.')

            if 'time' in query:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"the time is {strTime}")

            if 'date' in query:
                date()

            if 'make a note' in query:
                statement = statement.replace("make a note", "")
                note(statement)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
        
        elif 'shutdown system' in query:
            speak("Hold On a Sec! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

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

        elif 'unlock screen' in query:
            speak("Unlocking the screen")
            pyautogui.press('shift')  

        elif 'exit' in query:
            speak("Exiting the program.")
        
        elif 'shutdown' in query:
            speak("Shut down the system.")
            break