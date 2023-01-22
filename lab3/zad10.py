radius = int(input("podaj promien koła: "))
a = radius
b = radius
y0 = -a
x0 = -b
for y in range(y0,radius+1):
    for x in range(x0,radius+1):
        d = (y/a)**2+(x/b)**2
        if d>=0.8 and d <= 1:
            print(' * ',end='')
        else:
            print('   ', end='')
    print('')
print('\n\n\n',end='')
for y in range(y0,radius+1):
    for x in range(x0,radius+1):
        d = (y/a)**2+(x/b)**2
        if d <= 1:
            print(' * ',end='')
        else:
            print('   ', end='')
    print('')
print('\n\n\n',end='')