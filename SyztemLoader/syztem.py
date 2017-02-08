import os
import time
import ast
class ISC: # It must be here too.
    def do(cmd):
        sz.logTo(sz.config["sDir"]+"\\log.txt", str(cmd))
        p = cmd.split()
        if p[0] in sz.SZdata:
            if sz.SZdata[p[0]]["type"]=="SCmd":
                sz.SCmdv2(p[0], p[1:])
            elif sz.SZdata[p[0]]["type"]=="SVar":
                if len(p)>1:
                    sz.SVar(p[0], p[1])
                else:
                    sz.SVar(p[0])
    def python(path):
        f = open(path, "r")
        sz.logTo(sz.config["sDir"]+"\\log.txt", "+Python file {}".format(path))
        sz.logTo(sz.config["sDir"]+"\\log.txt", f.readlines())
        sz.logTo(sz.config["sDir"]+"\\log.txt", "eof+")
        f.seek(0)
        exec(f.read())
        f.close()

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
                sz.SZdata[var]["value"] = value
            else:
                print(sz.SZdata[var]["value"])
        except:
            print("[!]Could not read variable.")
            
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