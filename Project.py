import pyttsx3 as p
import randfacts
import speech_recognition as sr
from selenium import webdriver
from YTplayer import *
from news import *
from randfacts import *
import subprocess
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_driver_path = (r'C:\Users\Hatem Ben Gamra\Desktop\Math\\chromedriver.exe')

class infow():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org")
        search = self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button/i')
        enter.click()


engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.say("Hello world. My name is Jarvis but I am also known as vision")
engine.say("At your service sir")
engine.runAndWait()


def speak(text):
    engine.say(text)
    engine.runAndWait()


r = sr.Recognizer()  # to recognize microphone as source

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening to you lord Hatem ...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

if "what" and "about" and "you" in text:
    speak("I am having a good day sir")
    speak("what can I do for you? ")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listening .. ")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)

if "information" in text2:
    speak(" you need information related to which topic?")

    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening .. ")
        audio = r.listen(source)
        information = r.recognize_google(audio)
    print("searching for {} in wikipidea".format(information))
    speak("searching for {} in wikipidea".format(information))
    assist = infow()
    assist.get_info(information)

elif"play" and "video" in text2:
    speak("you want me to play which video?")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening .. ")
        audio = r.listen(source)
        vid = r.recognize_google(audio)
    print("playing {} on youtube".format(vid))
    speak("playing {} on youtube".format(vid))
    assist = music()
    assist.play(vid)

elif "news" in text2:
    print("Sure sir, Now I will read the news for you")
    speak("Sure sir, Now I will read the news for you")
    arr=news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])

elif "fact" or "facts" in text2:
    speak("Sure sir")
    x = randfacts.get_fact()
    print(x)
    speak("Did you know that, " + x)

# CODE CHAIMAA

elif "write" or "note" in text2:
    speak("Sure sir")
    os.system('notepad.exe')  # starts notepad

elif "weather" in text2:
    speak("Sure sir")
    webbrowser.open('https://weather.com/weather/today', new=2)
