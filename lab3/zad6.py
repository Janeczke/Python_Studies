for i in range(0,10):
    for j in range(0,10):
        if i % 2 == 0 and j % 2 != 0:
            print("*", end = ' ')
        elif i % 2 != 0 and j % 2 == 0:
            print("*", end = ' ')
        else:
            print(" ", end = ' ')
    print("")