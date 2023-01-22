a= -1
b =0

for i in range(1000+1):
    c = (a + b) / 2
    if ((c ** 5 + c + 1) > 0 and (a ** 5 + a + 1) > 0)  or ((c ** 5 + c + 1) < 0 and a ** 5 + a + 1 < 0):
        a = c
    else:
        b = c
print(c)
print(c**5+c+1)