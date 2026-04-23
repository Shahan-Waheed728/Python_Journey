import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library
import requests
import time
is_speaking = False
recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "a0d26fd60f8a4c4eb43249aef51dd509"

def speak(text):
    global is_speaking
    is_speaking = True
    engine.say(text)
    engine.runAndWait()
    is_speaking = False

def processCommand(c):
      
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")

    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")

    elif "open chatgpt" in c.lower():
        webbrowser.open("https://www.chat.openai.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = music_library.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
           #Parse the JSON response          
           data = r.json()

           #Extract the articles
           articles = data.get("articles", [])
           #Print the heaslines
           
           for article in articles:
            speak(article['title'])
           


if __name__ == "__main__":
    speak("Initializing Jarvis")
    #Listen for the wake word "Jarvis"
    with sr.Microphone() as source:        
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Microphone calibrated for ambient noise.")
    while  True:  

        try:
            if is_speaking:
              time.sleep(0.1)
              continue
            with sr.Microphone() as source:
                print("Listening for wake word...")           
                audio = recognizer.listen(source, timeout=2,phrase_time_limit=3)
            word = recognizer.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yeah")   
                #Listen for command
                with sr.Microphone() as source:
                   print("Jarvis active...")
                   audio = recognizer.listen(source,timeout=2,phrase_time_limit=3) 
                   command = recognizer.recognize_google(audio)     
                   print("Command:",command)
                   processCommand(command)
                   time.sleep(0.5)

        except sr.WaitTimeoutError:
            pass   # user stayed silent
        except sr.UnknownValueError:
            pass   # unclear speech       
        except Exception as e:
            print("Error:",e)
          


