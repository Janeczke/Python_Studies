fo=open('test.txt','r')
while 1:
    s = fo.read(3)
    print(s)
    if s == '':
        break
fo.close() 