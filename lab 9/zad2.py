fo = open('Liczby.txt', 'r')
l = []
s = ''
while 1:
    x = fo.read(1)
    if x == '':
        break
    elif x == ' ':
        l.append(int(s))
        s = ''
    else:
        s += x
print(l)