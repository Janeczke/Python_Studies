for i in range(0,10):
    for j in range(0,10):
        if (i > 0 and i < 9) and (j > 0 and j < 9):
            print(" ", end = ' ')
        else:
            print("*", end = ' ')
    print("")