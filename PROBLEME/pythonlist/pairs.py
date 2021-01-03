# Program care gaseste toate perechile de intregi ale caror suma este egala cu un numar dat

lista = [x for x in range(0, 21)]
numarDat = 16

for i in range(len(lista) - 2):
    for j in range(i + 1, len(lista) - 1):
        if lista[i] + lista[j] == numarDat:
            print((lista[i],lista[j]))



    
        
