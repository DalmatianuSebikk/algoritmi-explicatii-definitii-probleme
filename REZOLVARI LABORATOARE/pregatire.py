"""
Folosind apeluri utile ale functiilor .find, .index, .count gasiti si afisati cele mai intalnite 10 cuvinte 
din fisierul cuvinte.in. Pentru acestea afisati pozitia primelor 3 aparitii (linie, indice).
Rulati primul cod pentru a descarca fisierul si apoi il gasiti in partea stanga, a patra iconita (Files).
"""

"""
from urllib.request import urlopen
import re

versuri = urlopen("http://www.romanianvoice.com/poezii/poezii/luceafarul.php").read()
versuri = "\n".join(
    versuri.decode("iso-8859-2")
    .replace("<br>", "")
    .replace("\n...\n", "")
    .splitlines()[64:553]
)

delimitatori = ",./?!@#$%^&*)_="

for delimitator in delimitatori:
    versuri = versuri.replace(delimitator, "")

listaCuvinte = versuri.split()

for i in range(len(listaCuvinte)):
    listaCuvinte[i] = listaCuvinte[i].lower()

listaTuple = []

for cuvant in listaCuvinte:
    tupla = (cuvant, listaCuvinte.count(cuvant))
    
    if tupla not in listaTuple:
        listaTuple.append(tupla)


def sortByValue(tupla):
    return tupla[1]

listaTuple = sorted(listaTuple, key=sortByValue, reverse=True)

for tupla in listaTuple:
    if tupla[0] == '-':
        listaTuple.pop(listaTuple.index(tupla))

listaCuvinte = []
for index in range(10):
    listaCuvinte.append(listaTuple[index][0])

d = {}
aparitii = [1] * 10
tuple_aparitii = [[] for _ in range(10)]

contor = 1
for linie in versuri.splitlines():
    for index in range(len(listaCuvinte)):
        if(linie.find(listaCuvinte[index]) != -1 and aparitii[index] <= 3):
            aparitii[index] += 1
            tuple_aparitii[index].append((contor, linie.find(listaCuvinte[index])))

    contor += 1

for index in range(10):
    print(listaCuvinte[index] + " apare de " + str(listaTuple[index][1]) + 
    " ori si cele 3 aparitii sunt: " + str(tuple_aparitii[index]))


# with open("versurimodif2.in", "wt", encoding="utf-8") as f:
#     f.write(str(listaTuple))
"""

from urllib.request import urlopen

versuri = urlopen("http://www.romanianvoice.com/poezii/poezii/luceafarul.php").read()
versuri = "\n".join(
    versuri.decode("iso-8859-2")
    .replace("<br>", "")
    .replace("\n...\n", "")
    .splitlines()[64:553]
)

# with open("versurimodif2.in", "wt", encoding="utf-8") as f:
#     f.write(str(listaTuple))