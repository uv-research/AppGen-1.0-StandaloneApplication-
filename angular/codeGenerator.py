import os
import sys
import shutil
import tkinter as tk
import pyttsx3

from angular.tslint import tslint
from angular.tsconfig import tsconfig
from angular.readme import readme
from angular.package import package
from angular.angular import angular
from angular.editorconfig import editorconfig
from angular.envenvironmentprod import envprod
from angular.envenvironment import env

from angular.src.tslint import srctslint
from angular.src.tsconfigspec import tsconfigspec
from angular.src.tsconfigapp import tsconfigapp
from angular.src.test import test
from angular.src.styles import styles
from angular.src.polyfills import polyfills
from angular.src.main import main
from angular.src.karmaconf import karmaconfig
from angular.src.index import index
from angular.src.browserslist import browserslist

from angular.app.routingmodule import routingmodule
from angular.app.componenthtml import *
from angular.app.componentcss import *
from angular.app.componentspec import componentspec
from angular.app.component import *
from angular.app.module import module

from angular.e2e.tsconfige2e import tsconfige2e
from angular.e2e.protractorconf import protractorconfig
from angular.e2e.srcappe2espec import srcappe2espec
from angular.e2e.srcapppo import srcapppo

engine = pyttsx3.init()
engine.setProperty('rate', 115)
engine.setProperty('volume', 0.9)

endPath = "./finalApp"

def initAngularCodeCreater(c, o, self):
    checkDir(c, o, self)

def checkDir(c, o, self):
    try:
        shutil.rmtree(endPath)
    except OSError:
        createFiles(c,o, self)
    else:
        createFiles(c,o, self)

def createFiles(z,x, self):
    try:
        os.makedirs(endPath)
        os.makedirs("./finalApp/e2e")
        os.makedirs("./finalApp/e2e/src")
        os.makedirs("./finalApp/src")
        os.makedirs("./finalApp/src/app")
        os.makedirs("./finalApp/src/assets")
        os.makedirs("./finalApp/src/environments")
        
        a11 = open("./finalApp/.editorconfig","w+")
        a11.write(editorconfig)
        a11.close()
        a12 = open("./finalApp/angular.json","w+")
        a12.write(angular)
        a12.close()
        a13 = open("./finalApp/package.json","w+")
        a13.write(package)
        a13.close()
        a14 = open("./finalApp/README.md","w+")
        a14.write(readme)
        a14.close()
        a15 = open("./finalApp/tsconfig.json","w+")
        a15.write(tsconfig)
        a15.close()
        a16 = open("./finalApp/tslint.json","w+")
        a16.write(tslint)
        a16.close()

        a21 = open("./finalApp/e2e/protractor.conf.js","w+")
        a21.write(protractorconfig)
        a21.close()
        a22 = open("./finalApp/e2e/tsconfig.e2e.json","w+")
        a22.write(tsconfige2e)
        a22.close()
        a23 = open("./finalApp/e2e/src/app.e2e-spec.ts","w+")
        a23.write(srcappe2espec)
        a23.close()
        a24 = open("./finalApp/e2e/src/app.po.ts","w+")
        a24.write(srcapppo)
        a24.close()

        a31 = open("./finalApp/src/environments/environment.prod.ts","w+")
        a31.write(envprod)
        a31.close()
        a32 = open("./finalApp/src/environments/environment.ts","w+")
        a32.write(env)
        a32.close()

        a41 = open("./finalApp/src/app/app-routing.module.ts","w+")
        a41.write(routingmodule)
        a41.close()
        a42 = open("./finalApp/src/app/app.component.html","w+")
        a42.close()
        a43 = open("./finalApp/src/app/app.component.scss","w+")
        a43.close()
        a44 = open("./finalApp/src/app/app.component.spec.ts","w+")
        a44.write(componentspec)
        a44.close()
        a45 = open("./finalApp/src/app/app.component.ts","w+")
        a45.close()
        a46 = open("./finalApp/src/app/app.module.ts","w+")
        a46.write(module)
        a46.close()

        a50 = open("./finalApp/src/browserslist","w+")
        a50.write(browserslist)
        a50.close()
        a51 = open("./finalApp/src/index.html","w+")
        a51.write(index)
        a51.close()
        a52 = open("./finalApp/src/karma.conf.js","w+")
        a52.write(karmaconfig)
        a52.close()
        a53 = open("./finalApp/src/main.ts","w+")
        a53.write(main)
        a53.close()
        a54 = open("./finalApp/src/polyfills.ts","w+")
        a54.write(polyfills)
        a54.close()
        a55 = open("./finalApp/src/styles.scss","w+")
        a55.write(styles)
        a55.close()
        a56 = open("./finalApp/src/test.ts","w+")
        a56.write(test)
        a56.close()
        a57 = open("./finalApp/src/tsconfig.app.json","w+")
        a57.write(tsconfigapp)
        a57.close()
        a58 = open("./finalApp/src/tsconfig.spec.json","w+")
        a58.write(tsconfigspec)
        a58.close()
        a59 = open("./finalApp/src/tslint.json","w+")
        a59.write(srctslint)
        a59.close()

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
        generate(z,x, self)

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

        writeHtmlPart1()
        for d in range(0, count):
            writeInputs(d)
        writeHtmlPart2()
        
        writeComponentPart1()
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
        self.conversation.insert(tk.END,""".
.
.
Application successfully Created.\n"""
        )
        if self.getVoiceAssistance:
            engine.say("Application successfully Created")
            engine.runAndWait()
