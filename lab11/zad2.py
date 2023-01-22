
def zera(a,b): 
    return [[0 for i in range(a)] for j in range(b)]

def id(n): 
    return [[1 if i==j else 0 for i in range(n)] for j in range(n)] 
    
def wyswietl(A): 
    for i in range(len(A)): 
        for j in range(len(A[i])): 
            print(A[i][j], end=' ') 
        print() 
    print('\n') 

print('zera(3,4) = ') 
wyswietl(zera(3,4)) 

print('id(3) = ') 
wyswietl(id(3))