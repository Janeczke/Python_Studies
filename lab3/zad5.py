x = 0
y = 9
for i in range(0,10):
    for j in range(0,10):
        if (i > 0 and i < 9) and (j > 0 and j < 9):
            if j == x or j == y:
                print("*", end = ' ')

            else:
                print(" ", end = ' ')
        else:
            print("*", end = ' ')
    x+=1
    y-=1
    print("")