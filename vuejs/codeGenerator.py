import os
import sys
import shutil
import tkinter as tk
import pyttsx3

from vuejs.AppVue import *
from vuejs.babelConfig import *
from vuejs.baseComponent import *
from vuejs.indexHtml import *
from vuejs.mainJs import *
from vuejs.packageJson import *
from vuejs.README import *

engine = pyttsx3.init()
engine.setProperty('rate', 115)
engine.setProperty('volume', 0.9)

endPath = "./finalApp"

def initVuejsCodeCreater(c, o, self):
    checkDir(c, o, self)

def checkDir(c, o, self):
    try:
        shutil.rmtree(endPath)
    except OSError:
        createFiles(c,o,self)
    else:
        createFiles(c,o,self)

def createFiles(z,x,self):
    try:
        os.makedirs(endPath)
        os.makedirs("./finalApp/public")
        os.makedirs("./finalApp/src")
        os.makedirs("./finalApp/src/assets")
        os.makedirs("./finalApp/src/components")
        a = open("./finalApp/package.json","w+")
        a.write(package)
        a.close()
        b = open("./finalApp/README.md","w+")
        b.write(readme)
        b.close()
        c = open("./finalApp/babel.config.js","w+")
        c.write(bable)
        c.close()
        d = open("./finalApp/public/index.html","w+")
        d.write(indexhtml)
        d.close()
        e = open("./finalApp/src/App.vue","w+")
        e.write(appvue)
        e.close()
        f = open("./finalApp/src/main.js","w+")
        f.write(main)
        f.close()
        g = open("./finalApp/src/components/HelloWorld.vue","w+")
        g.close()

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
        generate(z,x,self)

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
        writePart1()
        for d in range(0, count):
            writeInputs(d)
        writePart2()
        for e in range(0, count):
            writeInData(e)
        writePart3()
        if operation == "add":
            writeAddOperation(count)
        elif operation == "addition":
            writeAddOperation(count)
        elif operation == "sum":
            writeAddOperation(count)
        elif operation == "difference":
            writeSubOperation(count)
        elif operation == "subtract":
            writeSubOperation(count)
        elif operation == "subtraction":
            writeSubOperation(count)
        writePart4()
        self.conversation.insert(tk.END,""".
.
.
Application successfully Created.\n"""
        )
        if self.getVoiceAssistance:
            engine.say("Application successfully Created")
            engine.runAndWait()