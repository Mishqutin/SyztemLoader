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

# Get data from load.txt and turn it into dictionary.
f = open("load.txt", "r")
config = lEval(f.read())
f.close()
sz.config = config

sz.logTo(config["sDir"]+"\\log.txt" ,time.strftime("### %d/%m/%Y--%H:%M:%S ###"))   # Start logging
# Change directory.
os.chdir("{}\\{}".format(config["sDir"], "data\\config\\autorun"))
for i in os.listdir():
    if i[-3:]==".py":
        try:
            ISC.python(i) # Execute string from every file in cwd.
        except:
            print("[!]Error at {} in autorun!".format(i))
for i in os.listdir():
    if i[-3:]==".sz":
        f = open(i, "r")
        for y in f.readlines():
            if not y[0]=="#":   # Hash acts like a comment.
                ISC.do(y)
        f.close()
    elif i[-3:]==".py":
        pass
    else:
        print("[!]Non-executable file format! {}".format(i))

os.chdir("{}\\{}".format(config["sDir"], config["first"]))
# Execute boot.sz in earlier selected directory (A, B or C)
f = open("boot.sz", "r")
for y in f.readlines():
    if not y[0]=="#":
        sz.logTo(config["sDir"]+"\\log.txt", str(y))
        ISC.do(y)
f.close()
# It is 10.02.2017, 18:26 GMT+0 - I need to take a shit.