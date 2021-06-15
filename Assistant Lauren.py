import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

print ("Initializing Lauren")

boss = "Abhinav"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#speak the fucntion written in form of text
def speak(text):
     engine.say(text)
     engine.runAndWait()
#this fucntion will wish you adn introduce as per time
def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour <12:
        speak('Good Morning' + boss)
    elif hour>=12 and hour <18:
        speak('Good Afternoon' + boss)
    else:
        speak('Good Evening' + boss)
    
    speak("I am Lauren, How may I help you?")
#this command wil take commands from microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")     
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said:{query}\n")  

    except Exception as e:
        print("Say that again please")
        query = None
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmail.com", "password") #password not recommended
    server.sendmail("recipents@gmail.com", to, content)
    server.close()

#Main Program starts here...
def main():
    speak ("Initializing Lauren")
    wishme()  
    query = takeCommand()

    #Logic for executing tasks as per query
    if 'wikipedia' in query.lower():
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences = 2)
        print(results)
        speak(results)

    elif 'open youtube' in query.lower():
        # webbrowser.open("youtube.com")
        url = "youtube.com"
        chrome_path = "C:\Users\Abhinav Anand\Desktop %s"
        webbrowser.get(chrome_path).open(url)

    elif 'open google' in query.lower():
        # webbrowser.open("google.com")
        url = "google.com"
        chrome_path = "C:\Users\Abhinav Anand\Desktop %s"
        webbrowser.get(chrome_path).open(url)

    elif 'open instagram' in query.lower():
        # webbrowser.open("youtube.com")
        url = "instagram.com"
        chrome_path = "C:\Users\Abhinav Anand\Desktop %s"
        webbrowser.get(chrome_path).open(url)

    elif 'play songs' in query.lower():
        song_dir = "..........." #enter the url of your folder in which songs are there
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(song_dir, songs[0]))

    elif "time" in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{boss} the time is {strTime}")

    elif "email to xyz" in query.lower():
        try:
            speak("what should i send")
            content = takeCommand()
            to = "xyz@gmail.com"
            sendEmail(to, content)
            speak("Email sent sucessfully")
        
        except Exception as e:
            print(e)

main()