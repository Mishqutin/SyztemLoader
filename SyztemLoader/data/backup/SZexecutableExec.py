import os
import sys
from ISClib import ISC
import ast
import time
import msvcrt

# Reads given file and executes it.

print("ISC compiler v0.1")

path = str(sys.argv[1])
try:
    f = open(path, "r")
except:
    print("File corrupted!")
    exit()
f.seek(0)
for i in f.readlines():
    param = i.split()
    if param[0]=="sleep":
        ISC.sleep(param[1])
    elif param[0]=="clear":
        ISC.cls()
    elif param[0]=="input":
        ISC.input()
    elif param[0]=="print":
        ISC.outstr(i[7:])
    elif param[0]=="outvar":
        ISC.output(param[1])
    elif param[0]=="nl":
        ISC.printNewLine()
    elif param[0]=="getkey":
        ISC.getkey()
    elif param[1]=="exe":
        ISC.call(param[0])
    elif 