fo = open('test.txt','r')
al = input('podaj slowo: ')
while 1:
    s = fo.readline()
    if al in s:
        print(s)
    if s == '':
        break
fo.close() 