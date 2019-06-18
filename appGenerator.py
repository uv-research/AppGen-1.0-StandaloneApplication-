import os
import sys
import pyttsx3
import tkinter as tk
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

from js.codeGenerator import initJsCodeCreater
from vuejs.codeGenerator import initVuejsCodeCreater
from angular.codeGenerator import initAngularCodeCreater

engine = pyttsx3.init()
engine.setProperty('rate', 115)
engine.setProperty('volume', 0.9)

endPath = "./finalApp"

class codekey:
    operation = ''
    count = ''
    language = ''

key = codekey()

operationList = ['add','addition','sum','difference','subtract','subtraction']

language = ['javascript','vuejs','reactjs','angular']

def startGenerator(inputData, self):
        splitData = inputData.split(" ")
        identifyKeyWords(splitData, self)

def identifyKeyWords(data, self):
    for a in data:
        try:
            val = int(a)
            key.count = val
        except ValueError:
            if a == data:
                print('no count') 
        
        for b in operationList:
            if a == b:
                key.operation = a
        
        for c in language:
            if a == c:
                key.language = onStackIdentification(self)

def onStackIdentification(self):
    if key.language == 'javascript':
        self.conversation.insert(tk.END,""".
.
.
Bot started coding in javascript \n"""
        )
        if self.getVoiceAssistance:
            engine.say("Bot started coding in javascript")
            engine.runAndWait()
        initJsCodeCreater(key.count, key.operation, self)

    elif key.language == 'vuejs':
        self.conversation.insert(tk.END,""".
.
.
Bot started coding in vuejs \n"""
        )
        if self.getVoiceAssistance:
            engine.say("Bot started coding in vuejs")
            engine.runAndWait()
        initVuejsCodeCreater(key.count, key.operation, self)
    
    elif key.language == 'angular':
        self.conversation.insert(tk.END,""".
.
.
Bot started coding in angular \n"""
        )
        if self.getVoiceAssistance:
            engine.say("Bot started coding in angular")
            engine.runAndWait()
        initAngularCodeCreater(key.count, key.operation, self)
    else:
        self.conversation.insert(tk.END,""".
.
.
sorry! The bot is not yet trained to create app in this language. will train it as soon as possible.\n"""
        )
        
        if self.getVoiceAssistance:
            engine.say("sorry! The bot is not yet trained to create application in this language. will train it as soon as possible.")
            engine.runAndWait()
