from msvcrt import getch
import time
import os
import sys
from syztem import sz
from syztem import ISC
from ast import literal_eval as lEval
import syztem
# There was some shit. I will make comments more readable soon -_-
os.system("cls")

# Boot - Get text from load.txt and convert it to dictionary for later use.
f = open("load.txt", "r")
config = lEval(f.read())
f.close()
sz.config = config

sz.logTo(config["sDir"]+"\\log.txt" ,time.strftime("### %d/%m/%Y--%H:%M:%S ###"))   # Start logging
# Go to directory where all the config is located and load it.
os.chdir("{}\\{}".format(config["sDir"], "data\\config\\autorun"))
for i in os.listdir():
    if i[-3:]==".py":
        try:
            ISC.python(i) # From every file get content and exec() it.
                            # In this form everything is placed in syztem scope.
        except:
            print("[!]Error at {} in autorun!".format(i))
for i in os.listdir():
    if i[-3:]==".sz":
        f = open(i, "r")
        for y in f.readlines():
            if not y[0]=="#":   # If line starts with '#' then ignore it. Acts like a comment.
                ISC.do(y)   # What is ISC I have wrote in README.MD.
        f.close()
    elif i[-3:]==".py":
        pass
    else:
        print("[!]Non-executable file format! {}".format(i))

os.chdir("{}\\{}".format(config["sDir"], config["first"]))
#try:
f = open("boot.sz", "r")
for y in f.readlines():
    if not y[0]=="#":
        sz.logTo(config["sDir"]+"\\log.txt", str(y))
        ISC.do(y)
f.close()
#except:
#    print("[!]Boot file unreadable!")