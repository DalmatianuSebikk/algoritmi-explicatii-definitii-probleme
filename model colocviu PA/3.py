"""
Nume: Ionel
Prenume: Sebastian
Grupa: 151
Subiect: 3
"""

# a)
def cifra_de_control(n):
    return n % 9

# b)
def insereaza_cifra_control(lista):

    lista_2 = []
    for element in lista:
        lista_2.append(cifra_de_control(element))

    index = 0
    for i in range(len(lista_2)):
        lista.insert(index + 1, lista_2[i])
        index += 2

# c)

def egale(*liste):

    lista = liste[0]

    for i in range(1, len(liste)):
        if liste[i] != lista:
            return False
    return True
        
# d)
numere = open("numere.in", "r").read().split()
lista_numere = [int(x) for x in numere]

    # insereaza_cifra_control(lista_numere)

    # for i in range(len(lista_numere)):
    #     if i % 2 == 0:
    #         print(lista_numere[i], lista_numere[i + 1], sep=' ')

# e)
d1 = {}
d2 = {}
numere2 = open("numere2.in", "r").read().split()
lista_numere2 = [int(x) for x in numere]

lista_numere_modif1 = []
lista_numere_modif2 = []

cif1 = []
cif2 = []

for numar in lista_numere:
    if numar not in d1:
        d1[numar] = True

for numar in lista_numere2:
    if numar not in d2:
        d2[numar] = True

for numar in d1:
    lista_numere_modif1.append(numar)

for numar in d2:
    lista_numere_modif2.append(numar)

insereaza_cifra_control(lista_numere_modif1)
insereaza_cifra_control(lista_numere_modif2)

for i in range(len(lista_numere_modif1)):
    if i % 2 == 1:
        cif1.append(lista_numere_modif1[i])

for i in range(len(lista_numere_modif2)):
    if i % 2 == 1:
        cif2.append(lista_numere_modif2[i])

print(egale(cif1, cif2))


