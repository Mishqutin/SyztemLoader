import os
import sys
import time
import ast
import subprocess
import msvcrt
import math
class ISC:
    def do(cmd):
        # sz.logTo(sz.config["sDir"]+"\\log.txt", str(cmd))
        try:
            p = cmd.split()
        except:
            pass
        if p[0] in sz.SZdata:
            if sz.SZdata[p[0]]["type"]=="SCmd":
                sz.SCmdv2(p[0], p[1:])
                
            elif sz.SZdata[p[0]]["type"]=="SVar":
                if len(p)>1:
                    sz.SZdata[p[0]]["value"] = SzDataEval(' '.join(p[1:]))
                else:
                    appendCI(sz.SZdata[p[0]]['value'])
                    return sz.SZdata[p[0]]['value']
        else:
            try:
                f = open(p[0]+".py", 'r')
                exec(f.read())
                f.close()
            except:
                try:
                    f = open(sz.config["sDir"]+"\\data\\home\\software\\"+p[0]+".py", 'r')
                    exec(f.read())
                    f.close()
                except:
                    try:
                        f = open(os.getenv('userprofile')+'\\documents\\Syztem\\prgs\\{}.py'.format(p[0]), 'r')
                        exec(f.read())
                        f.close()
                    except:
                        try:
                            if eval(cmd)!=None:
                                appendCI(eval(cmd))
                        except:
                            appendCI('ISC: Operation unsuccessful.')
    def python(path):
        f = open(path, "r")
        #sz.logTo(sz.config["sDir"]+"\\log.txt", "+Python file {}".format(path))
        #sz.logTo(sz.config["sDir"]+"\\log.txt", f.readlines())
        #sz.logTo(sz.config["sDir"]+"\\log.txt", "eof+")
        f.seek(0)
        exec(f.read())
        f.close()
    def endTask():
        errorGFHJKJHGFDFGHJKJHGFDFGHJKJHGFDSFGHJHGFDSDFGHJHGFDFGHJHGFDGHJHGFDFGHJHGFDFGHGFDFGHGFD
    def exeSzFull(path):
        try:
            ISC.exeSz(path)
        except:
            try:
                ISC.exeSz(sz.config["sDir"]+"\\data\\home\\software\\"+path)
            except:
                try:
                    ISC.exeSz(os.getenv('userprofile')+'\\documents\\Syztem\\prgs\\'+path)
                except:
                    appendCI("File does not exist or it is corrupted:")
                    appendCI(path)
    def exeSz(path):
        f = open(path)
        lines = f.readlines()
        f.close()
        labels = {}
        counter = 0
        for i in lines:
            if i[0]==":":
                labels[ i[ 1: ].replace( "\n", "" ) ] = counter
            counter += 1
        counter = 0
        gotoUsedThisLine = False

        while True:
            if counter>=len(lines): break
            i = lines[counter]
            
            if i!="" and i!="\n" and i:
                if i[0:3]=="if ":
                    params = i.split()
                    if params[2]=="goto":
                        if SzDataEval(params[1].replace(":", "")):
                            counter = labels[ params[3].replace("\n", "") ]
                            gotoUsedThisLine = True
                if i[0] == "#" or i[0] == ":": pass
                elif i[0:4] == "goto":
                    try:
                        counter = labels[ i[5:].replace("\n", "") ]
                    except:
                        appendCI("Wrong use of 'goto'.")
                        break
                
                    
                    
                    #appendCI( i[ i.find('goto') + 5: ].replace("\n", "") )
                else:
                    if gotoUsedThisLine: gotoUsedThisLine = False
                    else: ISC.do(i)
            #appendCI(counter)
            counter += 1
            refresh()


                


            

# Functions
def appendCI(txt):
    txt = str(txt).replace('\n', '')
    cmdInput=ast.literal_eval(sz.SZdata['cmdInput']['value'])
    line = ''
    for i in txt:
        if len(line)<68:
            line = line+i
        else:
            cmdInput.append(line)
            line = i
    cmdInput.append(line)
    sz.SZdata['cmdInput']['value']=str(cmdInput)

def listDir(path='.'):
    for i in os.listdir(path):
        appendCI(i)
def clearCI():
    sz.SZData("cmdInput", "SVar", '["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]')

def scrollUp():
    scroll = ast.literal_eval( sz.SZdata['currentPageScroll']['value'] )
    for i in range(len(scroll)):
        scroll[i]=scroll[i]-1
    sz.SZdata['currentPageScroll']['value'] = str(scroll)

def scrollDown():
    scroll = ast.literal_eval( sz.SZdata['currentPageScroll']['value'] )
    for i in range(len(scroll)):
        scroll[i]=scroll[i]+1
    sz.SZdata['currentPageScroll']['value'] = str(scroll)

def editSidebar(row, text):
    sidebar = ast.literal_eval(sz.SZdata['sidebarContent']['value'])
    sidebar[int(row)]=text
    sz.SZdata['sidebarContent']['value'] = str(sidebar)

def showFile(path):
    f = open(path, 'r')
    counter = 0
    for i in f.readlines():
        appendCI('{}| {}'.format(counter, i))
        counter += 1

def refresh():
    currentPageScroll = ast.literal_eval( sz.SZdata['currentPageScroll']['value'] )
    sidebar = ast.literal_eval(sz.SZdata['sidebarContent']['value'])
    cmdInput = ast.literal_eval(sz.SZdata["cmdInput"]["value"])
    ISC.do("cls")
    screen = """\
{}
--------------------------------------------------------------------|PyQutin
{: <68}|v0
{: <68}|
{: <68}|InDev
{: <68}|
{: <68}|
{: <68}|---------
{: <68}|{:.9}
{: <68}|{:.9}
{: <68}|{:.9}
{: <68}|{:.9}
{: <68}|{:.9}
{: <68}|{:.9}
{: <68}|{:.9}
{: <68}|{:.9}
{: <68}|{:.9}
{: <68}|{:.9}
{: <68}|{:.9}
{: <68}|{:.9}
{: <68}|{:.9}
{: <68}|{:.9}
{: <68}|{:.9}
--------------------------------------------------------------------^---------""".format( os.getcwd()+" "*(68-len( os.getcwd() ))+"|==", cmdInput[ currentPageScroll[20] ], cmdInput[ currentPageScroll[19] ], cmdInput[ currentPageScroll[18] ], cmdInput[ currentPageScroll[17] ], cmdInput[ currentPageScroll[16] ], cmdInput[ currentPageScroll[15] ], cmdInput[ currentPageScroll[14] ], sidebar[0], cmdInput[ currentPageScroll[13] ], sidebar[1], cmdInput[ currentPageScroll[12] ], sidebar[2], cmdInput[ currentPageScroll[11] ], sidebar[3], cmdInput[ currentPageScroll[10] ], sidebar[4], cmdInput[ currentPageScroll[9] ], sidebar[5], cmdInput[ currentPageScroll[8] ], sidebar[6], cmdInput[ currentPageScroll[7] ], sidebar[7], cmdInput[ currentPageScroll[6] ], sidebar[8], cmdInput[ currentPageScroll[5] ], sidebar[9], cmdInput[ currentPageScroll[4] ], sidebar[10], cmdInput[ currentPageScroll[3] ], sidebar[11], cmdInput[ currentPageScroll[2] ], sidebar[12], cmdInput[ currentPageScroll[1] ], sidebar[13], cmdInput[ currentPageScroll[0] ], sidebar[14])
    print(screen)

def SzDataEval(string):

    for i in sz.SZdata:
        if '$'+i in string:
            if type(sz.SZdata[i]['value'])==int: string = string.replace('$'+i, str(sz.SZdata[i]['value']))
            if type(sz.SZdata[i]['value'])==str: string = string.replace('$'+i, "'"+str(sz.SZdata[i]['value'])+"'")
    return eval(string)

def output(string):

    for i in sz.SZdata:
        if '$'+i in string:
            string = string.replace('$'+i, str(sz.SZdata[i]['value']))
    appendCI(string)

def defSet(targetName, value):
    try:
        f = open("{}\\documents\\Syztem\\settings\\defs.txt".format(os.getenv('userprofile')), 'r')
        sets = ast.literal_eval(f.read())
        f.close()
        sets[targetName] = value
        os.system('del {}\\documents\\Syztem\\settings\\defs.txt'.format(os.getenv('userprofile')))
        f = open("{}\\documents\\Syztem\\settings\\defs.txt".format(os.getenv('userprofile')), 'w')
        f.write(str(sets))
        f.close()
        
    except:
        if type(targetName)==str: appendCI("Could not set default value of {}".format(targetName))
        else: appendCI("Could not set setting's default value.")

def programRestart():
    os.system('start {}\\syz.bat'.format(config['sDir']))
    exit()

def getKey(var):
    sz.SZData(str(var), "SVar", msvcrt.getch().decode('UTF-8'))

def inputString(var):
    sz.SZData(str(var), "SVar", input())

def doIf(value, cmd):
    if SzDataEval(value): ISC.do(cmd)

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
            if value!=None:
                exec('sz.SZdata[var]["value"] = {}'.format(value))
            else:
                return sz.SZdata[var]["value"]
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
    
