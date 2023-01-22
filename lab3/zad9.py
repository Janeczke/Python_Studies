for i in range (1 , 11):
    for j in range(1, 11):
        if j == 1:
            if i == 10:
                print(i, end=' ')
            else:
                print(i, end=' ')

        elif i == 1:
            print(j, end=' ')

        elif i**j > j**i:
            print(">", end=' ')

        elif i**j == j**i:
            print("=", end=' ')
        else:
            print("<", end=' ')
    print("")