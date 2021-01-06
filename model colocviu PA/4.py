"""
Nume: Ionel
Prenume: Sebastian
Grupa: 151
Subiect: 4
"""

# a)

fisier = open("fisier.txt", "r")
lista_elemente = fisier.read().split('\n')
dictionar_spiridusi = {}

for element in lista_elemente:
    if element == '':
        lista_elemente.pop(lista_elemente.index(element))


for spiridus in lista_elemente:

    lista_stringuri = spiridus.split()
    lista_stringuri[1] = int(lista_stringuri[1])
    lista_de_bagat_in_dictionar = []
    string = ""

    for i in range(2, len(lista_stringuri)):
        string += lista_stringuri[i]
        string += ' '

    string = string[:len(string) - 1] # ca sa elimin spatiul
    
    tupla = (lista_stringuri[1], string)
    lista_de_bagat_in_dictionar.append(tupla)

    if lista_stringuri[0] not in dictionar_spiridusi:
        dictionar_spiridusi[lista_stringuri[0]] = lista_de_bagat_in_dictionar
    else:
        dictionar_spiridusi[lista_stringuri[0]].append(tupla)


# b)

def despre_spiridus(structura, cod):
    lista = structura[cod]

    for i in range(len(lista)):
        # inversez tupla ca asa vrea ghimis
        lista[i] = lista[i][::-1]

    def pentru_sortat(tupla):
        return -tupla[1], tupla[0]

    lista = sorted(lista, key=pentru_sortat)

    return lista


# c)
def jucarii(structura):
    lista = []
    dictionar_aparitii_jucarii = {}
    for element in structura:
        for tuplu in structura[element]:
            if tuplu[1] not in dictionar_aparitii_jucarii:
                lista.append(tuplu[1])
                dictionar_aparitii_jucarii[tuplu[1]] = True
    
    string = ""
    for jucarie in lista:
        string += jucarie
        string += ","
    string = string[:len(string) - 1]

    return string

# d)

def spiridusi(structura):
    lista_tupluri = []

    for element in structura:
        nr_bucati_jucarii = 0
        lista = structura[element]
        jucarii_distincte = len(lista)

        for tuplu in lista:
            nr_bucati_jucarii += tuplu[0]
        
        lista_tupluri.append((element, jucarii_distincte, nr_bucati_jucarii))

    def pentru_sortat(tuplu):
        return -tuplu[1], -tuplu[2], tuplu[0]

    lista_tupluri = sorted(lista_tupluri, key=pentru_sortat)

    for tuplu in lista_tupluri:
        print(tuplu)


def actualizare(structura, cod, nume_jucarie):
    numar_jucarii_distincte = len(structura[cod])

    if numar_jucarii_distincte > 2:
        for tuplu in structura[cod]:
            if tuplu[1] == nume_jucarie:
                structura[cod].pop(structura[cod].index(tuplu))
                return True
    else:
        return False

print(actualizare(dictionar_spiridusi, 'S1', 'trenulet'))
print(dictionar_spiridusi['S1'])


    