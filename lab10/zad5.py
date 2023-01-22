sl={"zielony":"green","czapka":"cap","niebo":"sky","robak":"worm","strona":"page"}
l1=list(sl.values())
l2=list(sl.keys())
a=0
fo=open("slownik.txt","w+", encoding='utf-8')
for i in l1:
    fo.write(l1[a])
    fo.write(":")
    fo.write(l2[a])
    fo.write(";")
    a+=1
fo.close()