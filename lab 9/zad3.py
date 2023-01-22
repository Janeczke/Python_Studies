import random
def los():
    a=random.randrange(1,6)
    if a == 1:
        return True
fo=open('gwiazdki.txt','w')
for i in range(1,2501):
    if i%50==0:
        fo.write("\n")
    elif los() is True:
        fo.write("*")
    else:
        fo.write(" ")
fo.close()