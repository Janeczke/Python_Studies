import random
fo=open('liczby.txt','w+')
for i in range(20):
    fo.write(str(random.randint(1,100)))
fo.write(' ')
fo.close()