if p[1]=="write":
    f = open(os.getenv('userprofile')+'\\documents\\Syztem\\notes\\'+p[2]+'.txt', 'w')
    editSidebar(0, 'To exit')
    editSidebar(1, 'type in')
    editSidebar(2, '@end')
    editSidebar(3, 'on the')
    editSidebar(4, 'last line')
    while True:
        refresh()
        x = input()
        if sz.SZdata['echo']['value']==1: appendCI(x)
        if x=="@end":
            break
        f.write(x+'\n')
    f.close()
elif p[1]=="read":
    showFile(os.getenv('userprofile')+'\\documents\\Syztem\\notes\\'+p[2]+'.txt')
elif p[1]=="list":
    listDir(os.getenv('userprofile')+'\\documents\\Syztem\\notes')

editSidebar(0, '')
editSidebar(1, '')
editSidebar(2, '')
editSidebar(3, '')
editSidebar(4, '')