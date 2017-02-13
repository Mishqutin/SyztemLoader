editorCmd = { 'help':"ISC.do('mode help')", 'edit':"ISC.do('mode edit')", 'exit':'troll', 'save':"f = open(p[1], 'w')\nf.write(''.join(lines))\nf.close()\n"}
f = open(p[1], 'r')
lines = f.readlines()
f.close()

while True:
    mode = sz.SZdata['termMode']['value']
    if mode == 'console':
        editSidebar(0, 'Text')
        editSidebar(1, 'Editor')
        editSidebar(2, 'Type in')
        editSidebar(3, 'help')
        editSidebar(4, 'for help')
        clearCI()
        lineCounter = 0
        for line in lines:
            appendCI("{}| {}".format(lineCounter, line))
            lineCounter += 1
        refresh()
        x = input()
        if x:
            try:
                param = x.split()
            except:
                pass
            exec(editorCmd[param[0]])
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
    elif mode == "help":
        clearCI()
        appendCI("Commands:")
        appendCI("edit <line number> - Edits line.")
        appendCI("exit - Exit without saving.")
        appendCI("save - Save.")
        refresh()
        x = input()
        ISC.do("mode console")
    elif mode == "edit":
        clearCI()
        appendCI("Old string:")
        appendCI(lines[ int(param[1]) ])
        refresh()
        x = input()
        if x:
            lines[ int(param[1]) ] = x+'\n'
        ISC.do("mode console")
    