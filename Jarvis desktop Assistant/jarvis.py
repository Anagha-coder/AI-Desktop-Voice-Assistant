
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia # to access wikipedia
import webbrowser
import os
import random
import smtplib



engine = pyttsx3.init('sapi5')  #used to take the voices 
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)   
    if hour>= 0 and hour<12:
        speak("Good Morning Anagha!")

    elif hour>=12 and hour <18:
        speak("Good Afternoon Anagha!") 

    else:
        speak("Good evening Anagha!") 

    speak("I'm Jarvis, How may I help you?")       

def takeCommand():
    # It takes microphone input from the user and returns the string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 
        # pause_threshold is seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') 
        # print("User said: {query}\n") 
        print("User said: ",query)

    except Exception as e:
        print("Sorry couldn't recognize you. Please say that again...")
        return "None"       

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('anaghaworktest11@gmail.com','RAM89011a')
    server.sendmail('anaghaworktest11@gmail.com',to,content) 
    server.close()


if __name__ == "__main__":
    # speak("Anagha you're pretty")
    wishMe()
    
    while True:
    
        query = takeCommand().lower()

        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com") 

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'open whatsapp' in query:
            webbrowser.open("web.whatsapp.com")       

        elif 'open spotify' in query: # or desktop music can use random module 
            webbrowser.open("spotify.com") 

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%h:%M:%S")
            speak(f"current time is {strTime}") 

        elif 'open code' in query:
            codePath = "C:\\Users\\adesa\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)     

        elif 'play movie' in query:
            p="F:\series\MANIFEST"
            os.chdir(p)

            # print(os.listdir(p))
            folder_name = random.choice(os.listdir(p))

            folder_path = str(os.path.realpath(folder_name))
            os.chdir(folder_path)
            file_name = random.choice(os.listdir(folder_path))

            print("Enjoy!")

            # play to file

            #os.system("open " + file_name) # mac
            os.system("start " + file_name) # window
            

        elif 'how are you jarvis' in query:
            speak("I'm good!, How you doin?")

        elif 'thank u jarvis' in query:
            speak("my pleasure to serve you")  

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "adesai38711@gmail.com"
                sendEmail(to,content)
                speak("Email ha been sent!")
            except Exception as e:
                print(e)
                speak("Sorry coudn't send email at the moment.")




         

        
            
    

        

            
            


                           