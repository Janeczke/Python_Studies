def odwr(sl):
    l1=list(sl.values())
    l2=list(sl.keys())
    sl2={}
    if len(l1) > len(set(l1)):
        print("Słownik zawiera powtórzenia!")
        return 0
    else:
        for i in range(0,len(l1)):
            sl2[l1[i]]=l2[i]
    return sl2
sl={"zielony":"green","czapka":"cap","niebo":"sky","robak":"worm","strona":"page"}
print(sl)
print(odwr(sl))