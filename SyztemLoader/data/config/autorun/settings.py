#try:
f = open("{}\\documents\\Syztem\\settings\\defs.txt".format(os.getenv('userprofile')), 'r')
a = eval(f.read())
color = int(a["termColor"])
os.system('color {}'.format(color))
#except:
    #print('File defs.txt: cannot read termColor')