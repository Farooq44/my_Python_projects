# importing mondule
import SpeechRecognition as sr
import webbrowser
import os
import pyttsx3
import datetime

# create engine for text to speech
engine = pyttsx3.init()

# speak function
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# take command functions
def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining.....")
        audio = listener.listen(source)
        try:
            command = listener.recognize_google(audio)
            command = command.lower()
            print("your said: ", command)
            return command
        except:
            return ""
# run assistant
def run_assistant():
    command = take_command()
    # if command contains time
    if 'time' in command:
        time = datetime.datetime.time()
        speak("Current time is:", time)
        print("Current time is:", time)
    # if command contains open notepad
    elif 'open notepad' in command:
        speak("Opening Notepad")
        print("Openig notepad")
        os.system('notepad')
    
    # if command contains open youtube
    elif 'open youtube' in command:
        speak('Opening youtube')
        print("Opening youtube")
        webbrowser.open("https://www.youtube.com")
    # if command contains hey siri
    elif 'hey siri' in command:
        query = command.replace("hey siri", "")
        if query:
            url = f"https://www.google.com/search?q={query}"
            speak(f"Searching for {query}")
            print(f"Searching for {query}")
            webbrowser.open(url)
    # if command conatains stop
    elif 'stop' in command:
        speak("Okay, bye bye see u again")
        exit()
    else:
        print("I am here to assist you ask like current time, open \
              youtube, sesrch for somthing.....")

# main 
if __name__ == "__main__":
    name = input("Enter your name:", )
    speak(f"Hey hi {name}, I am here to assist you ask like current time, open \
              youtube, sesrch for somthing.....")
    while True:
        run_assistant()

