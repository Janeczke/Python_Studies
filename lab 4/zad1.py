for i in 'To jest zdanie': print(i, end='*')
print()
text = input('Podaj zdanie: ')
x=0
for i in text:
    print(i, end=' ')
    x+=2
print(f'\nLiczba znaków to {x}')
x = 0
