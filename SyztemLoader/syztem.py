import os
import ast


class sz:

    def SZexecutable(path): # ToDo: Args
        os.system("python {}{} {}".format(sz.getConfig()["sDir"], "\\data\\stools\\SZexecutableExec.py", path))
    def getConfig():
        return ast.literal_eval(os.environ["SZconfig"])