"""
Nume: Ionel
Prenume: Sebastian
Grupa: 151
Subiect: 1
"""

# a)
def min_max(lista):
    return (min(lista), max(lista))


# b)
def citire(nume):
    f = open(nume, "r")

    lista = f.read().split('\n')
    listaGoala = []
    listaDeAdaugat = []

    for string in lista:
        listaDeAdaugat = string.split()

        if len(listaDeAdaugat) != 0:
            for i in range(len(listaDeAdaugat)):
                listaDeAdaugat[i] = int(listaDeAdaugat[i])

            listaGoala.append(listaDeAdaugat)

    return listaGoala

# c)

fisier_citit = input("Numele fisierului: ")
fisier_scris = open("egale.txt", "w")
xs = citire(fisier_citit)

for i in range(len(xs)):
    tupla = min_max(xs[i])

    if tupla[0] == tupla[1]:
        string = str(i)
        string += '\n'
        fisier_scris.write(string)

lista_minimi = []
lista_maximi = []

for lista in xs:
    tupla = min_max(lista)
    lista_minimi.append(tupla[0])
    lista_maximi.append(tupla[1])

print("a = " + str(min(lista_minimi)) + ", b = " + str(max(lista_maximi)))









