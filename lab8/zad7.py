fo = open('test.txt','r')
f1 = open('test2.txt', 'w')
while 1:
    s = fo.read(1)
    f1.write(s.upper())
    if s == '':
        break
fo.close() 