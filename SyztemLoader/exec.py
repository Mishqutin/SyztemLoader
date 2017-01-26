from msvcrt import getch
import os
import sys
from syztem import sz
from ast import literal_eval as lEval
class ISC:
    def do(cmd):    # cmd must be a string
        p = cmd.split()
        if p[0] in sz.SZdata:   # check if it's defined
            if sz.SZdata[p[0]]["type"]=="SCmd": # Check if its is SCmd..
                sz.SCmdv2(p[0], p[1:])
            elif sz.SZdata[p[0]]["type"]=="SVar":   # ..or SVar.
                if len(p)>1:    # If any arguments were passed.
                    sz.SVar(p[0], p[1])
                else:
                    sz.SVar(p[0])
    def python(path):   # executes Python files
        f = open(path, "r")
        exec(f.read())
        f.close()
os.system("cls")

# Boot - Get txt from load.txt and convert it to dictionary for later use.
f = open("load.txt", "r")
config = lEval(f.read())
f.close()

# Go to directory where all the config is located and load it.
os.chdir("{}\\{}".format(config["sDir"], "data\\config\\autorun"))
for i in os.listdir():
    if i[-3:]==".py":
        try:
            f = open(i, "r")
            exec(f.read())  # From every file get content and exec() it.
            f.close()       # In this form everything is placed in local scope.
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
        ISC.do(y)
f.close()
#except:
#    print("[!]Boot file unreadable!")