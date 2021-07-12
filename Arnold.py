import pyttsx3  #pip install pyttsx3
import datetime  #module
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia #pip install wikipedia
import smtplib
import pywhatkit #pip install pywhatkit
import wolframalpha #pip install wolframalpha
import webbrowser as wb
import os  #inbuilt
import pyautogui #pip install PyAutoGUI
import psutil  #pip install psutil
import pyjokes  #pip install pyjokes
import requests, json

engine = pyttsx3.init()
engine.setProperty('rate', 190)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('volume', 1)


#Change voice

def voice_change(v):
    x = int(v)
    engine.setProperty('voice', voices[x].id)
    speak("done sir")


#Speak Function

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#Time Function

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    print(Time)
    speak(Time)


#Date Function

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    print("The current date is")
    speak("The current date is")
    print(date)
    speak(date)
    print(month)
    speak(month)
    print(year)
    speak(year)


def checktime(tt):
    hour = datetime.datetime.now().hour
    if ("morning" in tt):
        if (hour >= 6 and hour < 12):
            print("Good morning sir")
            speak("Good morning sir")
        else:
            if (hour >= 12 and hour < 18):
                print("it's Good afternoon sir")
                speak("it's Good afternoon sir")
            elif (hour >= 18 and hour < 24):
                print("it's Good Evening sir")
                speak("it's Good Evening sir")
            else:
                print("it's Goodnight sir")
                speak("it's Goodnight sir")
    elif ("afternoon" in tt):
        if (hour >= 12 and hour < 18):
            print("it's Good afternoon sir")
            speak("it's Good afternoon sir")
        else:
            if (hour >= 6 and hour < 12):
                print("Good morning sir")
                speak("Good morning sir")
            elif (hour >= 18 and hour < 24):
                print("it's Good Evening sir")
                speak("it's Good Evening sir")
            else:
                print("it's Goodnight sir")
                speak("it's Goodnight sir")
    else:
        print("it's night sir!")
        speak("it's night sir!")


#Welcome Function

def wishme():
    print("Welcome Back")
    speak("Welcome Back")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        print("Good Morning sir!")
        speak("Good Morning sir!")
    elif (hour >= 12 and hour < 18):
        print("Good afternoon sir")
        speak("Good afternoon sir")
    elif (hour >= 18 and hour < 24):
        print("Good Evening Sir!")
        speak("Good Evening Sir!")
    else:
        print("Goodnight Sir!")
        speak("Goodnight Sir!")

    print("Arnold at your service, Please tell me how can i help you?")
    speak("Arnold at your service, Please tell me how can i help you?")


def wishme_end():
    print("signing off")
    speak("signing off")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        print("Good Morning")
        speak("Good Morning")
    elif (hour >= 12 and hour < 18):
        print("Good afternoon")
        speak("Good afternoon")
    elif (hour >= 18 and hour < 24):
        print("Good Evening")
        speak("Good Evening")
    else:
        print("Goodnight.. Sweet dreams")
        speak("Goodnight.. Sweet dreams")
    quit()


#Command by User Function

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        #speak(query)
        print(query)
    except Exception as e:
        print(e)
        print("Say that again please...")
        speak("Say that again please...")

        return "None"

    return query


#Sending Email Function

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("username@gmail.com", "password")
    server.sendmail("username@gmail.com", to, content)
    server.close()


#Screenshot Function

def screenshot():
    img = pyautogui.screenshot()
    img.save(r"C:\Users\GANESH KUMAR M A\Pictures\ss.png")


#Battery and Cpu Usage

def cpu():
    usage = str(psutil.cpu_percent())
    print('CPU usage is at ' + usage)
    speak('CPU usage is at ' + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
    print("battery is at:" + str(battery.percent))


#Joke Function

def jokes():
    j = pyjokes.get_joke()
    print(j)
    speak(j)


#Weather Condition

def weather():
    api_key = "API KEY" #generate your own api key from open weather
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    speak("tell me which city")
    city_name = takeCommand()
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        r = ("in " + city_name + " Temperature is " +
             str(int(current_temperature - 273.15)) + " degree celsius " +
             ", atmospheric pressure " + str(current_pressure) + " hpa unit" +
             ", humidity is " + str(current_humidiy) + " percent"
             " and " + str(weather_description))
        print(r)
        speak(r)
    else:
        speak(" City Not Found ")


def personal():
    print("I am Arnold, version 1.0, I am an Digital Assistant, I am here to help you")
    speak("I am Arnold, version 1.0, I am an Digital Assistant, I am here to help you")


if __name__ == "__main__":
    wishme()
    while (True):
        query = takeCommand().lower()

#Time

        if ('time' in query):
            time()

#Date

        elif ('date' in query):
            date()

#Personal Info

        elif ("tell me about yourself" in query):
            personal()
        elif ("about you" in query):
            personal()
        elif ("who are you" in query):
            personal()
        elif ("yourself" in query):
            personal()

#Searching on Wikipedia

        elif ('wikipedia' in query):
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=3)
            print(query)
            print(result)
            speak(result)

#Sending Email

        elif ("send email" in query):
            try:
                print("What is the message ?")
                speak("What is the message ?")
                content = takeCommand()
                print("Who is the Receiver?")
                speak("Who is the Receiver?")
                receiver = ("Enter Receiver's Email : ")
                to = receiver
                speak("Email has sent")
            except Exception as e:
                print(e)
                speak("Unable to send email check the address of the recipient.")

#Search On Google

        elif ("search on google" in query or "open website" in query):
            print("What should i search or open?")
            speak("What should i search or open?")
            search = takeCommand().lower().split()
            print('Searching....')
            speak('Searching....')
            wb.open('https://www.google.com/search?q=' + '+'.join(search))

#Open Youtube
        elif ("search youtube" in query):
            query = query.replace("search youtube", "")
            print('playing ' + query)
            speak('playing ' + query)
            pywhatkit.playonyt(query)

#System Logout/ Shut Down etc

        elif ("logout" in query):
            os.system("shutdown -1")
        elif ("restart" in query):
            os.system("shutdown /r /t 1")
        elif ("shut down" in query):
            os.system("shutdown /r /t 1")

#Play Songs

        elif ("play songs" in query):
            print("Playing...")
            speak("Playing...")
            songs_dir = r"C:\Users\GANESH KUMAR M A\Music"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[1]))

#Play Videos

        elif ("play videos" in query):
            print("Playing...")
            speak("Playing...")
            videos_dir = r"C:\Users\GANESH KUMAR M A\Videos"
            videos = os.listdir(videos_dir)
            os.startfile(os.path.join(videos_dir, videos[1]))

#Reminder Function

        elif ("create a reminder list" in query or "reminder" in query):
            print("What is the reminder?")
            speak("What is the reminder?")
            data = takeCommand()
            print("You said to remember that " + data)
            speak("You said to remember that " + data)
            reminder_file = open("data.txt", 'a')
            reminder_file.write('\n')
            reminder_file.write(data)
            reminder_file.close()

#Reading Reminder List

        elif ("do you know anything" in query or "remember" in query):
            reminder_file = open("data.txt", 'r')
            print("You said me to remember that: " + reminder_file.read())
            speak("You said me to remember that: " + reminder_file.read())

#Screenshot

        elif ("screenshot" in query):
            screenshot()
            print("Done!")
            speak("Done!")

#Searching using wolframalpha

        elif ("what is" in query or "who is" in query):
            client = wolframalpha.Client("API KEY") #generate your own api key from open wolfram alpha
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No Results")

#Cpu and Battery Usage

        elif ("cpu and battery" in query or "battery" in query
              or "cpu" in query):
            cpu()

#Jokes

        elif ("tell me a joke" in query or "joke" in query):
            jokes()

#Weather

        elif ("weather" in query or "temperature" in query):
            weather()

#Location
        elif 'where is' in query:
            query = query.replace('where is', '')
            location = query
            print("You asked to locate" + location)
            speak("You asked to locate" + location)
            wb.open_new_tab("https://www.google.com/maps/place/" + location)

#Arnold features

        elif ("tell me your uses" in query or "help" in query
              or "features" in query):
            features = ''' I can help to do lot many things like..
            i can tell you the current time and date,
            i can tell you the current weather,
            i can tell you battery and cpu usage,
            i can create the reminder list,
            i can take screenshots,
            i can send email to who you wish,
            i can shut down or logout or hibernate your system,
            i can tell you funny jokes,
            i can open any website,
            i can locate any place,
            i can search the anything on youtube,
            i can search the anything on wikipedia,
            i can change my voice from male to female and vice-versa
            And so on...
            '''
            print(features)
            speak(features)

        elif ("hii" in query or "hello" in query or "good morning" in query
              or "good afternoon" in query or "good night" in query
              or "morning" in query or "noon" in query or "night" in query):
            query = query.replace("arnold", "")
            query = query.replace("hi", "")
            query = query.replace("hello", "")
            if ("morning" in query or "night" in query or "goodnight" in query
                    or "afternoon" in query or "noon" in query):
                checktime(query)
            else:
                speak("what can i do for you")

#Changing voice
        elif ("voice" in query):
            print("for female say f and, for male say m")
            speak("for female say f and, for male say m")
            q = takeCommand()
            if ("f" in q):
                voice_change(1)
                print("Done Sir!")
            elif ("m" in q):
                voice_change(0)
                print("Done Sir!")
        elif ("m" in query or "f" in query):
            if ("f" in query):
                voice_change(1)
                print("Done Sir!")
            elif ("m" in query):
                voice_change(0)
                print("Done Sir!")

#exit function

        elif ('I am done' in query or 'bye bye arnold' in query
              or 'go offline' in query or 'bye' in query
              or 'nothing' in query):
            wishme_end()
