# import pyttsx3 
# import speech_recognition as sr 
# import datetime
# import wikipedia
# import webbrowser
# import subprocess
# import os
# import winshell
# import win32gui
# import win32con
# import ctypes
# import pyautogui
# import requests
# from googleapiclient.discovery import build


# pyautogui.FAILSAFE = False

# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

# def wishMe():
#     hour = int(datetime.datetime.now().hour)
#     if hour>=0 and hour<12:
#         speak("Hello, Good Morning!, Please tell me how may I help you")
#     elif hour>=12 and hour<18:
#         speak("Hello, Good Afternoon!, Please tell me how may I help you")   
#     else:
#         speak("Hello, Good Evening!, Please tell me how may I help you")  

# def takeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source)

#     try:
#         print("Recognizing...")    
#         query = r.recognize_google(audio, language='en-in')
#         print(f"User said: {query}\n")

#     except Exception as e:
#         print("Say that again please...")  
#         return "None"
#     return query


# def sleep_computer():
#     win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND, win32con.SC_MONITORPOWER, 2)

# def wakeup_computer():
#     if ctypes.windll.kernel32.GetSystemPowerStatus(ctypes.byref(ctypes.c_ulong())) == 0:
#         pass

# def lock_pc():
#     ctypes.windll.user32.LockWorkStation()

# def is_locked():
#     return ctypes.windll.user32.GetForegroundWindow() == 0

# def unlock_pc(pin):
#     if is_locked():
#         original_pos = pyautogui.position()
#         pyautogui.write(pin)
#         pyautogui.press('enter')
#         pyautogui.moveTo(original_pos[0] + 1, original_pos[1])
#     else:
#         speak("The system is not locked.")

# def getWeather(city):

#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=465e7077dc6c658d4245771eb8dd0057&units=metric"
    
#     response = requests.get(url)
#     data = response.json()
    
#     if data['cod'] != '404':
#         weather = data['main']
#         temperature = weather['temp']
#         humidity = weather['humidity']
#         weather_desc = data['weather'][0]['description']
#         speak(f"The temperature in {city} is {temperature} degrees Celsius with {weather_desc} and humidity of {humidity}%.")
#     else:
#         speak("City not found. Please try again.")

# def getNews():

#     url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey=f64723fe578345e8a89706ae69fd9c03"
    
#     response = requests.get(url)
#     data = response.json()
    
#     articles = data['articles']
#     for idx, article in enumerate(articles):
#         if idx < 5:  
#             speak(article['title'])

# def searchYouTube(query):
#     # api_key = os.environ.get('YOUTUBE_API_KEY')
#     # if not api_key:
#     #     speak("YouTube Data API key is not set.")
#     #     return

#     url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&key=AIzaSyCVIb0_BzRSkeqJFLUYhXPAlsLyEqRIyxM"
    
#     response = requests.get(url)
#     data = response.json()
    
#     videos = data['items']
#     if videos:
#         video = videos[0] 
#         video_title = video['snippet']['title']
#         video_url = f"https://www.youtube.com/watch?v={video['id']['videoId']}"
#         speak(f"I found a video titled {video_title}. Would you like me to open it?")
#     else:
#         speak("No videos found for the given query.")

# # def getCricketScores():
# #     headers = {
# #         'X-RapidAPI-Key': '8f8c10c19cmshc934eef8567a32ep1eea52jsna556b39ec894',
# #         'X-RapidAPI-Host': 'cricket24.p.rapidapi.com'
# #     }

# #     url = 'https://cricket24.p.rapidapi.comhttps//dev132-cricket-live-scores-v1.p.rapidapi.com/matches.php'

# #     try:
# #         response = requests.get(url, headers=headers)
# #         data = response.json()
# #         print(data)  # You may want to process and speak the cricket match data here
# #     except Exception as e:
# #         print("Error fetching cricket data:", e)

# if _name_ == "_main_":
#     wishMe()
#     while True:
#         query = takeCommand().lower()
        
#         if 'wikipedia' in query:
#             speak('Searching Wikipedia...')
#             query = query.replace("wikipedia", "")
#             results = wikipedia.summary(query, sentences=1)
#             speak("According to Wikipedia")
#             speak(results)
        
#         elif 'open youtube' in query:
#             webbrowser.open("youtube.com")

#         elif 'open google' in query:
#             webbrowser.open("google.com")

#         elif 'open stackoverflow' in query:
#             webbrowser.open("stackoverflow.com")   
        
#         elif 'shutdown system' in query:
#             speak("shut down")
#             subprocess.call('shutdown / p /f')

#         elif "restart" in query:
#             subprocess.call(["shutdown", "/r"])
                 
#         elif 'empty recycle bin' in query:
#             winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
#             speak("Recycle Bin Recycled")

#         elif 'the time' in query:
#             strTime = datetime.datetime.now().strftime("%H:%M:%S")    
#             speak(f"Sir, the time is {strTime}")

#         elif "where is" in query:
#             query = query.replace("where is", "")
#             location = query
#             speak("User asked to Locate")
#             speak(location)
#             webbrowser.open("https://www.google.nl/maps/place/"+location+"")

#         elif 'search' in query or 'play' in query:
#             query = query.replace("search", "")
#             query = query.replace("play", "")         
#             webbrowser.open(query)

#         elif 'sleep' in query:
#             sleep_computer()
#             speak("System is going to sleep")

#         elif 'wake up' in query:
#             wakeup_computer()
#             speak("System is waking up")

#         elif 'lock pc' in query:
#             lock_pc()
#             speak("System is locked")

#         elif 'on' in query:
#             unlock_pc(pin)

#         elif 'email to mansi' in query:
#             try:
#                 speak("What should I say?")
#                 content = takeCommand()
#                 to = "manshipatel131415@gmail.com"    
#                 sendEmail(to, content)
#                 speak("Email has been sent!")
#             except Exception as e:
#                 print(e)
#                 speak("Sir i am not able to send this email")

#         elif 'get weather' in query:
#             speak("Sure, please tell me the city name.")
#             city = takeCommand().lower()
#             getWeather(city)

#         elif 'get news' in query:
#             getNews()

#         elif 'search youtube' in query:
#             speak("What do you want to search on YouTube?")
#             search_query = takeCommand().lower()
#             searchYouTube(search_query)

#         # elif 'get cricket scores' in query:
#         #     getCricketScores()

#         elif 'exit' in query:
#             speak("Exiting the program.")
#             break

import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import subprocess
import os
import winshell
import win32gui
import win32con
import ctypes
import pyautogui
import requests
from googleapiclient.discovery import build


pyautogui.FAILSAFE = False

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

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
        print("Say that again please...")  
        return "None"
    return query


def sleep_computer():
    win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND, win32con.SC_MONITORPOWER, 2)

def wakeup_computer():
    if ctypes.windll.kernel32.GetSystemPowerStatus(ctypes.byref(ctypes.c_ulong())) == 0:
        pass

def lock_pc():
    ctypes.windll.user32.LockWorkStation()

def is_locked():
    return ctypes.windll.user32.GetForegroundWindow() == 0
pin="0141"

def unlock_pc(pin):
    if is_locked():
        original_pos = pyautogui.position()
        pyautogui.write(pin)
        pyautogui.press('enter')
        pyautogui.moveTo(original_pos[0] + 1, original_pos[1])
    else:
        speak("The system is not locked.")
    

def getWeather(city):
    api_key = os.environ.get('OPENWEATHERMAP_API_KEY')
    if not api_key:
        speak("OpenWeatherMap API key is not set.")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=465e7077dc6c658d4245771eb8dd0057&units=metric"
    
    response = requests.get(url)
    data = response.json()
    
    if data['cod'] != '404':
        weather = data['main']
        temperature = weather['temp']
        humidity = weather['humidity']
        weather_desc = data['weather'][0]['description']
        speak(f"The temperature in {city} is {temperature} degrees Celsius with {weather_desc} and humidity of {humidity}%.")
    else:
        speak("City not found. Please try again.")

def getNews():
    # api_key = os.environ.get('NEWS_API_KEY')
    # if not api_key:
    #     speak("News API key is not set.")
    #     return

    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey=f64723fe578345e8a89706ae69fd9c03"
    
    response = requests.get(url)
    data = response.json()
    
    articles = data['articles']
    for idx, article in enumerate(articles):
        if idx < 5:  
            speak(article['title'])

def searchYouTube(query):
    

    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&key=AIzaSyCVIb0_BzRSkeqJFLUYhXPAlsLyEqRIyxM"
    
    response = requests.get(url)
    data = response.json()
    
    videos = data['items']
    if videos:
        video = videos[0] 
        video_title = video['snippet']['title']
        video_url = f"https://www.youtube.com/watch?v={video['id']['videoId']}"
        speak(f"I found a video titled {video_title}. Would you like me to open it?")
    else:
        speak("No videos found for the given query.")

# def getCricketScores():
#     headers = {
#         'X-RapidAPI-Key': '8f8c10c19cmshc934eef8567a32ep1eea52jsna556b39ec894',
#         'X-RapidAPI-Host': 'cricket24.p.rapidapi.com'
#     }

#     url = 'https://cricket24.p.rapidapi.comhttps//dev132-cricket-live-scores-v1.p.rapidapi.com/matches.php'

#     try:
#         response = requests.get(url, headers=headers)
#         data = response.json()
#         print(data)  # You may want to process and speak the cricket match data here
#     except Exception as e:
#         print("Error fetching cricket data:", e)

if __name__ == "__main__w":
    wishMe()
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            speak(results)
        

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

        elif 'time' in query:
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

        elif 'sleep' in query:
            sleep_computer()
            speak("System is going to sleep")

        elif 'wake up' in query:
            wakeup_computer()
            speak("System is waking up")

        elif 'lock pc' in query:
            lock_pc()
            speak("System is locked")

        elif 'on' in query:
            unlock_pc(pin)

        elif 'get weather' in query:
            speak("Sure, please tell me the city name.")
            city = takeCommand().lower()
            getWeather(city)

        elif 'latest news' in query:
            getNews()

        elif 'search youtube' in query:
            speak("What do you want to search on YouTube?")
            search_query = takeCommand().lower()
            searchYouTube(search_query)

        # elif 'get cricket scores' in query:
        #     getCricketScores()

        elif 'exit' in query:
            speak("Exiting the program.")
            break