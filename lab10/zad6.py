fo=open("slownik.txt","r+",encoding="utf-8")
sl={}
l1=[]
l2=[]
a=""
l1=fo.readline().split(";")
l1.pop()
for ele in l1:
    l2=ele.split(":")
    sl[l2[0]]=l2[1]
print(sl)
fo.close()