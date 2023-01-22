ln0, pi0 = 0.693147, 3.141593
ln, pi= 0,0
znak = -1
x=1
for n in range(1,10**5+1):
    ln += (1/n)*znak**(n+1)
for n in range(1,10**5+1,2):
    pi += 4*((1/n)*znak**(x+1))
    x +=1
print(f'obliczona liczba pi: {pi}')
print(f'obliczony ln(2): {ln}')