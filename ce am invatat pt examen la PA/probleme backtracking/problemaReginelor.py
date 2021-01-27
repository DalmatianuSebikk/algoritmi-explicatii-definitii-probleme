"""
Sa se plaseze N regine pe o tabla de sah n*n astfel incat oricare 2 regine sa nu se atace
"""

n = int(input())
tabla = [0] * n


def printf():
    for i in range(n):
        for j in range(n):
            if j == tabla[i]:
                print("*", end=" ")
            else:
                print("o", end=" ")
        print("", end='\n')
    print("\n")

def bkt(k, n):
    if k == n:
        printf()
    else:
        for i in range(n):
            # verific daca pot plasa regina pe linia k
            ok = 1
            for j in  range(k):
                if tabla[j] == i or abs(tabla[j] - i) == (k - j):
                    ok = 0
                    break
            
            if ok == 1:
                tabla[k] = i
                bkt(k + 1, n)

bkt(0, n)


    
