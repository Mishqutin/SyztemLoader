f = open("{}\\documents\\Syztem\\settings\\defs.txt".format(os.getenv('userprofile')), 'r')
a = eval(f.read())
color = int(a["termColor"])
os.system('color {}'.format(color))

makePause = open("{}\\documents\\Syztem\\settings\\makePause.txt".format(os.getenv('userprofile')), 'w')
makePause.write(a["pauseOnExit"])
makePause.close()
f.close()