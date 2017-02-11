ISC.do("cls")
ISC.do("title Qutin")
print("""

#PBFSEP V0.1.0


                          SBPQ OS
(Early shit/Wczesne gowno)""")
time.sleep(0.75)
while True:
    currentPageScroll = ast.literal_eval( sz.SZdata['currentPageScroll']['value'] )
    sidebar = ast.literal_eval(sz.SZdata['sidebarContent']['value'])
    cmdInput = ast.literal_eval(sz.SZdata["cmdInput"]["value"])
    mode = sz.SZdata['termMode']['value']
    ISC.do("cls")
    screen = """\
{}
--------------------------------------------------------------------|Qutin
{: <68}|v0
{: <68}|
{: <68}|PreInDev
{: <68}|
{: <68}|LOL
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
    if mode == 'console':
        x = input()
        if x:
            ISC.do("output {}".format(x))
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