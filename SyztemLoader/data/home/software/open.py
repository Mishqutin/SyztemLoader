if p[1]:
    f = open(sz.config['sDir']+'\\data\\home\\user\\shortcuts\\'+p[1], 'r')
    a = f.read()
    f.close()
    os.system('start {}'.format(a))