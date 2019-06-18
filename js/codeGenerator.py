import os
import sys
import shutil
import tkinter as tk
import pyttsx3

from js.htmlTemp import *
from js.jsTemp import *

engine = pyttsx3.init()
engine.setProperty('rate', 115)
engine.setProperty('volume', 0.9)

endPath = "./finalApp"

def initJsCodeCreater(c, o, self):
    checkDir(c, o, self)

def checkDir(c, o, self):
    try:
        shutil.rmtree(endPath)
    except OSError:
        createFiles(c,o, self)
    else:
        createFiles(c,o, self)    

def createFiles(c,o, self):
    try:
        os.makedirs(endPath)
        a = open("./finalApp/index.html","w+")
        a.write(base)
        a.close()
        b = open("./finalApp/script.js","w+")
        b.close()

    except OSError:
        self.conversation.insert(tk.END,""".
.
.
the dir %s creation failed.\n""" %endPath
        )
        if self.getVoiceAssistance:
            engine.say("dir %s creation failed" % endPath)
            engine.runAndWait()
    else:
        self.conversation.insert(tk.END,""".
.
.
the dir %s is created successfully.\n""" %endPath
        )
        if self.getVoiceAssistance:
            engine.say("dir %s creation successfully" % endPath)
            engine.runAndWait()
        generate(c,o, self)

def generate(count, operation, self):
    if count:
        self.conversation.insert(tk.END,""".
.
.
processing.\n"""
        )
        if self.getVoiceAssistance:
            engine.say("processing")
            engine.runAndWait()

        for d in range(0, count):
            writeInput(d)
        writeSubmit()
        writeInit()
        writeSubmitFunction(count, operation)
        self.conversation.insert(tk.END,""".
.
.
Application successfully Created.\n"""
        )
        if self.getVoiceAssistance:
            engine.say("Application successfully Created")
            engine.runAndWait()
