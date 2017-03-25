if p[1] and p[2]:
    f = open(os.getenv('userprofile')+'\\documents\\Syztem\\shortcuts\\'+p[2], 'w')
    f.write(p[1])
    f.close()