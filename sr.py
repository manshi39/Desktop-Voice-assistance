import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def record_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        return command
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None

def confirm_command(command):
    speak("You said, " + command + ". Please confirm.")
    confirmed = record_voice()
    return confirmed.lower() == "yes"

def main():
    speak("Please speak your command.")
    command = record_voice()
    if command:
        confirmed = confirm_command(command)
        if confirmed:
            print("Command confirmed:", command)
            # Process the command here
        else:
            print("Command not confirmed. Please try again.")

if __name__ == "__main__":
    main()
