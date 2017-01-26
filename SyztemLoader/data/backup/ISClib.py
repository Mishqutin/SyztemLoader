import os
import time
import msvcrt
import ast

ISCkey = None

class ISC:
    def remove(path):
        os.system("del {}".format(str(path)))
        
    def call(path):
        os.system("call {}".format(str(path)))
        
    def setEnv(var, value):
        # os.environ[str(var)] = str(value)
        os.system("setx {} {} >> nul".format(str(var), str(value)))
    def set(name, value):
        globals()['%s' % name] = value

    def sleep(timeout):
        time.sleep(float(timeout))
        
    def outstr(string):
        print(str(string))
        
    def printNewLine():
        ISC.outstr("\n")
        
    def getkey():
        global ISCkey
        inpt = msvcrt.getch().decode("utf-8")
        ISCkey = inpt
        
    def output(var):
        print(globals()[var])
    
    def input():
        global ISCkey
        ISCkey = input()
    
    def cls():
        os.system("cls")