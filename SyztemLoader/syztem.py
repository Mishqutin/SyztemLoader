import os
import time
import ast
class ISC: # It must be here too.
    def do(cmd):
        sz.logTo(sz.config["sDir"]+"\\log.txt", str(cmd))
        try:
            p = cmd.split()
        except:
            pass
        if p[0] in sz.SZdata:
            if sz.SZdata[p[0]]["type"]=="SCmd":
                sz.SCmdv2(p[0], p[1:])
                
            elif sz.SZdata[p[0]]["type"]=="SVar":
                if len(p)>1:
                    sz.SVar(p[0], p[1])
                else:
                    appendCI(sz.SZdata[p[0]]['value'])
                    return sz.SZdata[p[0]]['value']
    def python(path):
        f = open(path, "r")
        sz.logTo(sz.config["sDir"]+"\\log.txt", "+Python file {}".format(path))
        sz.logTo(sz.config["sDir"]+"\\log.txt", f.readlines())
        sz.logTo(sz.config["sDir"]+"\\log.txt", "eof+")
        f.seek(0)
        exec(f.read())
        f.close()

# Functions
def appendCI(txt):
    cmdInput=ast.literal_eval(sz.SZdata['cmdInput']['value'])
    cmdInput.append(str(txt))
    del cmdInput[0]
    sz.SZdata['cmdInput']['value']=str(cmdInput)

def listDir():
    last = 0
    add = []
    for i in os.listdir():
        if len(add)>2:
            appendCI(add)
            add = []
        else:
            add.append(i)
    if add:
        appendCI(add)
def clearCI():
    sz.SZData("cmdInput", "SVar", '["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]')
class sz:
    SZdata = {}
    config = 0

    def getConfig():
        return ast.literal_eval(os.environ["SZconfig"])
    
    def SCmd(cmd, *args):
        try:
            exec(sz.SZdata[cmd]["value"])
        except:
            print("[!]Command cannot be executed.")
        
    def SCmdv2(cmd, arg):
#        try:
        args = []
        for i in arg:
            args.append(i)
        exec(sz.SZdata[cmd]["value"])
#        except:
#            print("[!]Command cannot be executed.")
        
    def SVar(var, value=None):
        try:
            if value:
                exec('sz.SZdata[var]["value"] = {}'.format(value))
            else:
                return sz.SZdata[var]["value"]
        except:
            print("[!]Could not read variable.")
    
    def getSVar(name):
        pass
            
    def SZData(name, type, value):
        sz.SZdata[name] = {"type": type, "value": value}
    
    def ExecSZEnv(path):
        f = open(path, "r")
        exec(f.read())  # From every file get content and exec() it.
        f.close()
    
    def logTo(path, text):
        os.system("echo {} >> {}".format(text, path))
    
    def showFile(path):
        os.system('type {}'.format(str(path)))
        print("\n")