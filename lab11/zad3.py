#zad2

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





#zad3

def losowa(a, b, n): 
    from random import randint 
    return [[randint(1,n) for i in range(a)] for j in range(b)] 
    
def dodaj(A, B): 
    if len(A) == len(B) and len(A[0]) == len(B[0]): 
        return [[A[i][j] + B[i][j] for j in range(len(A[i]))] for i in range(len(A))]

    else: 
        return 'Macierze nie są takich samych rozmiarów' 
        
print('losowa(3,4,10) = ') 
macierz1 = losowa(4,3,10) 
wyswietl(macierz1)

print('losowa(3,4,10) = ') 
macierz2 = losowa(4,3,10) 
wyswietl(macierz2) 

print('macierz1 + macierz2 = ') 
wyswietl(dodaj(macierz1, macierz2))






#zad4

def pomnoz(A, B): 
    if len(A) == len(B) and len(A[0]) == len(B[0]): 
        return [[A[i][j] * B[i][j] for j in range(len(A[i]))] for i in range(len(A))] 
    
    else:
        return 'Macierze nie są takich samych rozmiarów' 
        
macierz1 = losowa(2,2,10) 
wyswietl(macierz1) 

macierz2 = losowa(2,2,10) 
wyswietl(macierz2) 

print('macierz1 * macierz2 = ') 
wyswietl(pomnoz(macierz1, macierz2))




#zad5

def zamW(A, i, j): 
    A[i], A[j] = A[j], A[i] 
    return A 
    
wyswietl(macierz1) 
wyswietl(zamW(macierz1, 0, 1)) 

def przemW(A, i, k): 
    A[i] = [k * x for x in A[i]] 
    return A 
    
wyswietl(macierz1) 
wyswietl(przemW(macierz1, 0, 3)) 
def dodajW(A, i, j, k):
    A[i] = [A[i][x] + k * A[j][x] for x in range(len(A[i]))] 
    return A 

wyswietl(macierz1) 
wyswietl(dodajW(macierz1, 0, 1, 2))






#zad6

def det(A): 
    if len(A) == len(A[0]):

        if len(A) == 2: 
            return A[0][0] * A[1][1] - A[0][1] * A[1][0] 
        else: 
            return sum([(-1)**i * A[0][i] * det([[A[j][k] for k in range(len(A[j])) if k != i] for j in 
range(len(A)) if j != 0]) for i in range(len(A[0]))]) 
    else: 
        return 'Macierz nie jest kwadratowa' 
        
macierz1 = losowa(3,3,10) 
wyswietl(macierz1) 
print('Wyznacznik macierzy = ', det(macierz1))


