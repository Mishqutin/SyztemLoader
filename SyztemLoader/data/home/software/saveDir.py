if p[1] and p[2]:
    f = open(os.getenv('userprofile')+'\\documents\\Syztem\\shortcuts\\'+p[1], 'w')
    f.write(' '.join(p[2:]))
    f.close()