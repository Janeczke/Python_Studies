fo = open('test.txt','r')
f1 = open('test2.txt', 'w')
while 1:
    s = fo.read(1)
    if s == ' ':
        f1.write('*')
    else:
        f1.write(s)
    if s == '':
        break
fo.close() 
