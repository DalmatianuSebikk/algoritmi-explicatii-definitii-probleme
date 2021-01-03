# program care gaseste numarul lipsa dintr-o lista de numere de la 1 la 100
# Trick: foloseste suma Gauss

lista = [x for x in range(1, 101)]
lista2 = lista
lista2.remove(10)

def missingNumber(listaParametru):
    gauss = (100*101 // 2)
    sumaLista = sum(listaParametru)

    return gauss - sumaLista

print(missingNumber(lista2))