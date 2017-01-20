from msvcrt import getch
import os
from syztem import sz
from ast import literal_eval as lEval

# Boot - Get txt from file and convert it to dictionary
f = open("load.txt", "r")
config = lEval(f.read())
os.environ["SZconfig"] = str(config)
f.close()
os.chdir("{}\\{}".format(config["sDir"], config["first"]))
sz.SZexecutable("boot.sz")