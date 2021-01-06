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


"""
Folosind apeluri utile ale functiilor split si reverse si slice-uri inversati strofele poeziei. 
Ultima strofa devine - prima, penultima - a doua, samd. Salvati aceasta poezie in fisierul inversat.txt.
"""

"""
lista_strofe = versuri.split('\n\n')
strofa = []
string = ""

for i in range(len(lista_strofe)):
    strofa = lista_strofe[i].split('\n')
    strofa.reverse()

    for index in range(len(strofa)):
        strofa[index] += '\n'

    for vers in strofa:
        string += vers

    lista_strofe[i] = string
    string = ""


for i in range(len(lista_strofe)):
    lista_strofe[i] += "\n"

lista_strofe.reverse()

versuri2 = ""
catren = 1

for strofa in lista_strofe:   
    versuri2 += strofa
    catren += 1

with open("inversat.txt", "wt", encoding="utf-8") as f:
    f.write(versuri2)
"""
"""
Verificati daca exista vreun vers care sa contina un cuvant in poezia initiala si in cea inversata. 
Afisati versul linia in poezia initiala si in poezia inversata. -> Ghimis stii romana cat stiu eu chimie

Exemplu: Comparati versul "A fost odată ca-n poveşti," cu versul "Nemuritor şi rece.". 
Nu au cuvinte in comun. Mergeti mai departe: "A fost ca niciodată." cu "Ci eu în lumea mea mă simt", etc.

Folositi eventual functia zip.
"""

"""
delimitatori = ",./?!@#$%^&*)_="

for delimitator in delimitatori:
    versuri = versuri.replace(delimitator, "")
    versuri2 = versuri2.replace(delimitator, "")


lista_versuri = versuri.split('\n')
lista_versuri_poezie_inversata = versuri2.split('\n')

lista_versuri_temporar = []
for i in range(len(lista_versuri)):
    if lista_versuri[i] != '':
        lista_versuri_temporar.append(lista_versuri[i])

lista_versuri = lista_versuri_temporar

lista_versuri_temporar = []
for i in range(len(lista_versuri_poezie_inversata)):
    if lista_versuri_poezie_inversata[i] != '':
        lista_versuri_temporar.append(lista_versuri_poezie_inversata[i])

lista_versuri_poezie_inversata = lista_versuri_temporar

# with open("liste.in", "wt", encoding="utf-8") as f:
#     f.write(str(lista_versuri))

# with open("liste2.in", "wt", encoding="utf-8") as f:
#     f.write(str(lista_versuri_poezie_inversata))

for i in range(len(lista_versuri)):
    lista_versuri[i] = lista_versuri[i].replace('\n', '')
    lista_versuri[i] = lista_versuri[i].lower()
    lista_versuri_poezie_inversata[i] = lista_versuri_poezie_inversata[i].replace('\n', '')
    lista_versuri_poezie_inversata[i] = lista_versuri_poezie_inversata[i].lower()

for i in range(len(lista_versuri)):
    vers1 = lista_versuri[i].split()
    vers2 = lista_versuri_poezie_inversata[i].split()

    if '-' in vers1:
        vers1.pop(vers1.index('-'))
    
    if '-' in vers2:
        vers2.pop(vers2.index('-'))

    for cuvant in vers1:
        if cuvant in vers2:
            contor = 1
            versuri = versuri.lower()

            for linie in versuri.splitlines():
                linie = linie.split()

                if '-' in linie:
                    linie.pop(linie.index('-'))

                if linie == vers1: 
                    print("vers1: " + str(contor))

                if linie == vers2:
                    print("vers2: " + str(contor))

                contor += 1
            
            break
"""         

# Scrieti poezia in fiserul simplu.txt fara diacritice. Folositi functia translate pe string-uri.

"""
str1 = "ăĂâÂîÎşŞţŢșȘțȚ"
str2 = "aAaAiIsStTsstT"

table = versuri.maketrans(str1, str2)



with open("versurimodif2.in", "wt", encoding="utf-8") as f:
    f.write(versuri.translate(table))
"""

"""
Transformati fiecare strofa intr-o matrice care contine caracterul de ordine fiecarei litere excluzand 
spatiile si semnele de punctuatie - acestea devin 0.

Exemplu pentru prima strofa, prima coloana este: 65, 65, 68, 79.

Scrieti pozitia in poezie a versului care are cel mai mare produs al elementelor.
"""


lista_strofe = versuri.split('\n\n')

matrice_poezie = []
delimitatori = "!@#$%^&*()<>?/,. "

for strofa in lista_strofe:
    lista_versuri = strofa.split('\n')
    linie = []
    
    for i in range(len(lista_versuri)):
        for j in range(len(lista_versuri[i])):
            if lista_versuri[i][j] in delimitatori:
                linie.append(0)
            else:
                linie.append(ord(lista_versuri[i][j]))
        
        matrice_poezie.append(linie)
        linie = []


with open("matrix.txt", "wt", encoding="utf-8") as f:
    catren = 1
    for i in range(len(matrice_poezie)):
        if catren == 4:
            f.write(str(matrice_poezie[i]) + '\n\n')
            catren = 1
        else:
            f.write(str(matrice_poezie[i]) + '\n')
            catren += 1
        

