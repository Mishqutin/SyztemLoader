import os
import ast


class sz:
    SZdata = {}

    def getConfig():
        return ast.literal_eval(os.environ["SZconfig"])
    
    def SCmd(cmd, *args):
        try:
            exec(sz.SZdata[cmd]["value"])
        except:
            print("[!]Command cannot be executed.")
        
    def SCmdv2(cmd, arg):
        try:
            args = []
            for i in arg:
                args.append(ast.literal_eval(i))
            exec(sz.SZdata[cmd]["value"])
        except:
            print("[!]Command cannot be executed.")
        
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