for i in 'To jest zdanie': print(i, end='*')
print()
text = input('Podaj zdanie: ')
x=0
for i in text:
    print(i, end=' ')
    x+=2
print(f'\nLiczba znaków to {x}')

x=0

for i in text:
    print(i, end='')
    if i == 'a':
        x+=1
print(f'\nLiczba znaków "a" to {x}')

word = 0
text +=' '
for w in text:
    if w == ' ' or w == '\0':
        word+=1
print(f"'{text}' ma {word} słowa")