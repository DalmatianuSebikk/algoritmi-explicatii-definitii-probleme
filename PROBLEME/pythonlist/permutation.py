# Identifica (2 liste primite) daca una este permutarea celeilalte

lista1 = [1, 2, 3]
lista2 = [2, 3, 1]

lista1.sort()
lista2.sort()

if lista1 == lista2:
    print('DA')
else:
    print('NU')