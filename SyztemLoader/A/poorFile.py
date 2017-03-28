ISC.do("cls")
os.chdir("{}\\{}".format(sz.config["sDir"], "data\\home"))
ISC.do("title Qutin")

print("""

#PBFSEP V0.1.0


                          SBPQ OS
(Early shit/Wczesne gowno)""")
time.sleep(0.75)

try:
    f = open(sz.config["sDir"]+"\\data\\home\\user\\startup.txt")
    fileData = f.readlines()
    f.close()
    ISC.exeSzFull(fileData[0])
except:
    appendCI("Cannot execute startup file.")

while True:
    mode = sz.SZdata['termMode']['value']
    refresh()
    if mode == 'console':
        x = input()
        if x:
            if sz.SZdata['echo']['value']==1: appendCI('> '+x)
            ISC.do(x)
    elif mode == 'scroll':
        editSidebar(0, 'Scrolling')
        editSidebar(1, 'mode.')
        editSidebar(2, 'w - up')
        editSidebar(3, 's - down')
        editSidebar(4, 'q - exit')
        x = msvcrt.getch()
        if x == b'w':
            scrollUp()
        elif x == b's':
            scrollDown()
        elif x == b'q':
            sz.SZdata['termMode']['value'] = 'console'
            editSidebar(0, '')
            editSidebar(1, '')
            editSidebar(2, '')
            editSidebar(3, '')
            editSidebar(4, '')
    else:
        sz.SZdata['termMode']['value'] = 'console'