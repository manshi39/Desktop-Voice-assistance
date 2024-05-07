import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import smtplib
import bs4
import pyjokes
import time
import operator
import subprocess
import keyboard
import wolframalpha
import os
import winshell

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Function to record user's voice for authentication
def record_user_voice():
    recognizer = sr.Recognizer()
    num_hello = 0
    while num_hello < 4:
        with sr.Microphone() as source:
            print("Listening for 'hello'...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
        
        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio).lower()
            if 'hello' in text:
                num_hello += 1
                print(f"'hello' {num_hello} of 4 recognized.")
            else:
                print("Didn't hear 'hello'. Please say 'hello'.")

        except Exception as e:
            print("Didn't hear 'hello'. Please say 'hello'.")

        # Save the recorded voice as a reference
    with open("user_voice.wav", "wb") as f:
        f.write(audio.get_wav_data())

    if(num_hello==4):
        return True
    else:
        return False
    


# Function to authenticate user's voice
def authenticate_voice():
    recognizer = sr.Recognizer()
    with sr.AudioFile("user_voice.wav") as source:
        print("Listening for authentication...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    # Recognize voice
    try:
        print("Recognizing...")
        user_voice = recognizer.recognize_google(audio).lower()
        print(f"User voice: {user_voice}\n")
        if 'hello' in user_voice:
            return True
        else:
            return False
    except Exception as e:
        print("Voice authentication failed. Please try again.")
        return False

# Main speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Hello, Good Morning!, Please tell me how may I help you")
    elif hour>=12 and hour<18:
        speak("Hello, Good Afternoon!, Please tell me how may I help you")   
    else:
        speak("Hello, Good Evening!, Please tell me how may I help you")  

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

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)
    subprocess.Popen(["notepad.exe", file_name])

if __name__ == "__main__":
    flag=record_user_voice()
    if(flag==True):
        print("Authenticated")
    else:
        print("Not authenticated")
    """
    authenticated = authenticate_voice()
    if not authenticated:
        print("Voice authentication failed. Exiting.")
        exit()
    
    wishMe()
    while True:
        query = takeCommand().lower()
                # Command handling logic
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
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
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

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

        
        
        
        elif 'exit' in query:
            speak("Exiting the program.")
            break

        """
    