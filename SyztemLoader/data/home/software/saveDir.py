if p[1] and p[2]:
    f = open(sz.config['sDir']+'\\data\\home\\user\\shortcuts\\'+p[2], 'w')
    f.write(p[1])
    f.close()