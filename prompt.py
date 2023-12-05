from threading import Thread
import multiprocessing as mp
import speech_recognition as sr
import os
import sys
import time as t
import pyautogui as pg
import random
import requests
import keyboard
import pyttsx3
import pywhatkit as kit
import datetime
import wikipedia
import pyaudio
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.setProperty('rate', 160)
engine.setProperty('volume', 1.0)

def talk(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def voice_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                print(command)
    except:
        pass
    return command

def take_command():
    try:
        print('waiting...')
        command = input()
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing '+ song)
        kit.playonyt(song)
    elif 'incog search' in command:
        target = command.replace('incog search', '')
        os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')
        t.sleep(2)
        pg.hotkey('shift', 'ctrl', 'n')
        t.sleep(1)
        pg.write(target)
        pg.press('enter')
    elif 'voice mode' in command:
        while True:
            run_alexa_voice()
    elif 'translate' in command:
        texttarget = command.replace('translate', '')
        os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')
        t.sleep(2)
        pg.hotkey('shift', 'ctrl', 'n')
        t.sleep(1)
        pg.write('https://www.deepl.com/de/translator')
        pg.press('enter')
        t.sleep(3)
        pg.write(texttarget)
        pg.press('enter')
    elif 'google' in command:
        result = command.replace('google', '')
        kit.search(result)
    elif 'spam' in command:
        t.sleep(7)
        for i in range(20):
            text = command.replace('spam', '')
            pg.write(text)
            pg.press('enter')
        talk('Task finished!')
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'german search' in command:
        wikipedia.set_lang('de')
        engine.setProperty('voice', voices[1].id)
        result = command.replace('german search', '')
        info = wikipedia.summary(result, 3)
        talk(info)
        engine.setProperty('voice', voices[2].id)
    elif 'search' in command:
        result = command.replace('search', '')
        info = wikipedia.summary(result, 3)
        talk(info)
    elif 'love' in command:
        talk('I personally do not have feelings, but from what I found in the internet, Love is a very strong feeling of affection towards someone who you are romantically or sexually attracted to')
    elif 'are you single' in command:
        talk('I am')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'incog goto' in command:
        website = command.replace('incog goto', '')
        os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')
        t.sleep(2)
        pg.hotkey('shift', 'ctrl', 'n')
        t.sleep(1)
        pg.write(website)
        pg.press('enter')
    elif 'goto' in command:
        website = command.replace('goto', '')
        os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')
        t.sleep(1)
        pg.write(website)
        pg.press('enter')
    elif 'open all' in command:
        path = command.replace('open all', '')
        os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')
        t.sleep(2)
        pg.write('https://mail.uni-bonn.de/')
        pg.press('enter')
        t.sleep(3)
        pg.press('enter')
        t.sleep(1)
        pg.hotkey('ctrl', 't')
        t.sleep(1)
        pg.write('https://merry.ulb.uni-bonn.de/mrbs_studyplaces/day.php?area=1')
        pg.press('enter')
        t.sleep(1)
        pg.hotkey('ctrl', 't')
        t.sleep(1)
        pg.write('https://ecampus.uni-bonn.de/login.php?client_id=ecampus&cmd=force_login&lang=de')
        pg.press('enter')
    elif 'open chrome' in command:
        path = command.replace('open chrome', '')
        os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')
    elif 'open whatsapp' in command:
        path = command.replace('open whatsapp', '')
        os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')
        t.sleep(2)
        pg.write('https://web.whatsapp.com/')
        pg.press('enter')
    elif 'open alpro' in command:
        path = command.replace('open alpro', '')
        os.startfile('C:/Users/mic/OneDrive/Documents/001 VWL/Sem 3/Algorithmen'+ path)
    elif 'open mikro' in command:
        path = command.replace('open mikro', '')
        os.startfile('C:/Users/mic/OneDrive/Documents/001 VWL/Sem 3/Mikro B'+ path)
    elif 'open makro' in command:
        path = command.replace('open makro', '')
        os.startfile('C:/Users/mic/OneDrive/Documents/001 VWL/Sem 3/Makro A'+ path)
    elif 'open oko' in command:
        path = command.replace('open oko', '')
        os.startfile('C:/Users/mic/OneDrive/Documents/001 VWL/Sem 3/Ökonometrie'+ path)
    elif 'weather' in command:
        location = command.replace('weather in ', '')
        api_result = requests.get('http://api.weatherstack.com/current?access_key=0abe44396455525d8e07c2b263cfe7a2&query='+ location +'')
        api_response = api_result.json()
        time = api_response['location']['localtime']
        desc = api_response['current']['weather_descriptions']
        speed = api_response['current']['wind_speed']
        direc = api_response['current']['wind_dir']
        talk('Current temperature in %s is %d celsius degree' % (api_response['location']['name'], api_response['current']['temperature']))
        talk('Local time is '+ time +' and the weather is' + str(desc))
        talk('The current wind speed is '+ str(speed) +' kilometers per hour towards '+ direc)
        talk('The humidity level is %s percent and the visibility level is %d kilometers' % (api_response['current']['humidity'], api_response['current']['visibility']))
    elif 'thank you' in command or 'poweroff' in command or 'thanks' in command or 'bye' in command:
        talk('you are welcome, goodbye')
        exit()
    else:
        talk('Please say the command again.')

def run_alexa_voice():
    command = voice_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing '+ song)
        kit.playonyt(song)
    elif 'incog search' in command:
        target = command.replace('incog search', '')
        os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')
        t.sleep(2)
        pg.hotkey('shift', 'ctrl', 'n')
        t.sleep(1)
        pg.write(target)
        pg.press('enter')
    elif 'text mode' in command:
        while True:
            run_alexa()
    elif 'translate' in command:
        texttarget = command.replace('translate', '')
        os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')
        t.sleep(2)
        pg.hotkey('shift', 'ctrl', 'n')
        t.sleep(1)
        pg.write('https://www.deepl.com/de/translator')
        pg.press('enter')
        t.sleep(3)
        pg.write(texttarget)
        pg.press('enter')
    elif 'google' in command:
        result = command.replace('google', '')
        kit.search(result)
    elif 'handwrite' in command:
        text = command.replace('handwrite', '')
        kit.text_to_handwriting(text, 'img1.png')
        os.startfile('img1.png')
        talk('Task finished!')
    elif 'spam' in command:
        t.sleep(7)
        for i in range(20):
            text = command.replace('spam', '')
            pg.write(text)
            pg.press('enter')
        talk('Task finished!')
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'german search' in command:
        wikipedia.set_lang('de')
        engine.setProperty('voice', voices[1].id)
        result = command.replace('german search', '')
        info = wikipedia.summary(result, 3)
        talk(info)
        engine.setProperty('voice', voices[2].id)
    elif 'search' in command:
        result = command.replace('search', '')
        info = wikipedia.summary(result, 3)
        talk(info)
    elif 'love' in command:
        talk('I personally do not have feelings, but from what I found in the internet, Love is a very strong feeling of affection towards someone who you are romantically or sexually attracted to')
    elif 'are you single' in command:
        talk('I am')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'incog goto' in command:
        website = command.replace('incog goto', '')
        os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')
        t.sleep(2)
        pg.hotkey('shift', 'ctrl', 'n')
        t.sleep(1)
        pg.write(website)
        pg.press('enter')
    elif 'goto' in command:
        website = command.replace('goto', '')
        os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')
        t.sleep(1)
        pg.write(website)
        pg.press('enter')
    elif 'open all' in command:
        path = command.replace('open all', '')
        os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')
        t.sleep(2)
        pg.write('https://mail.uni-bonn.de/')
        pg.press('enter')
        t.sleep(3)
        pg.press('enter')
        t.sleep(1)
        pg.hotkey('ctrl', 't')
        t.sleep(1)
        pg.write('https://merry.ulb.uni-bonn.de/mrbs_studyplaces/day.php?area=1')
        pg.press('enter')
        t.sleep(1)
        pg.hotkey('ctrl', 't')
        t.sleep(1)
        pg.write('https://ecampus.uni-bonn.de/login.php?client_id=ecampus&cmd=force_login&lang=de')
        pg.press('enter')
    elif 'open chrome' in command:
        path = command.replace('open chrome', '')
        os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')
    elif 'open whatsapp' in command:
        path = command.replace('open whatsapp', '')
        os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')
        t.sleep(2)
        pg.write('https://web.whatsapp.com/')
        pg.press('enter')
    elif 'open alpro' in command:
        path = command.replace('open alpro', '')
        os.startfile('C:/Users/mic/OneDrive/Documents/001 VWL/Sem 3/Algorithmen'+ path)
    elif 'open mikro' in command:
        path = command.replace('open mikro', '')
        os.startfile('C:/Users/mic/OneDrive/Documents/001 VWL/Sem 3/Mikro B'+ path)
    elif 'open makro' in command:
        path = command.replace('open makro', '')
        os.startfile('C:/Users/mic/OneDrive/Documents/001 VWL/Sem 3/Makro A'+ path)
    elif 'open oko' in command:
        path = command.replace('open oko', '')
        os.startfile('C:/Users/mic/OneDrive/Documents/001 VWL/Sem 3/Ökonometrie'+ path)
    elif 'weather' in command:
        location = command.replace('weather in ', '')
        api_result = requests.get('http://api.weatherstack.com/current?access_key=0abe44396455525d8e07c2b263cfe7a2&query='+ location +'')
        api_response = api_result.json()
        time = api_response['location']['localtime']
        desc = api_response['current']['weather_descriptions']
        speed = api_response['current']['wind_speed']
        direc = api_response['current']['wind_dir']
        talk('Current temperature in %s is %d celsius degree' % (api_response['location']['name'], api_response['current']['temperature']))
        talk('Local time is '+ time +' and the weather is' + str(desc))
        talk('The current wind speed is '+ str(speed) +' kilometers per hour towards '+ direc)
        talk('The humidity level is %s percent and the visibility level is %d kilometers' % (api_response['current']['humidity'], api_response['current']['visibility']))
    elif 'thank you' in command or 'poweroff' in command or 'thanks' in command or 'bye' in command:
        talk('you are welcome, goodbye')
        exit()
    else:
        talk('Please say the command again.')

while True:
    run_alexa()
