if p[1]:
    f = open(os.getenv('userprofile')+'\\documents\\Syztem\\shortcuts\\'+p[1], 'r')
    a = f.read()
    f.close()
    os.system('start /I {}'.format(a))