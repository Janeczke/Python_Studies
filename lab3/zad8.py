for i in range(0,10):
    for j in range(0,10):
        if i < abs(j-4.5) or i > -abs(j-4.5)+9:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print("")