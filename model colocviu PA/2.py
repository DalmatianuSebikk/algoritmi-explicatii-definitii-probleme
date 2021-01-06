"""
Nume: Ionel
Prenume: Sebastian
Grupa: 151
Subiect: 2
"""

# a) 
def deviruseaza(propozitie):
    # : la fiecare cuvânt a interschimbat prima literă cu ultima
    # : apoi inversat ordinea în care cuvintele apar în propoziție

    lista_cuvinte_prop = propozitie.split()
    lista_cuvinte_bune = []

    for cuvant in lista_cuvinte_prop:
        cuvant_devirusat = ""

        if len(cuvant) == 1:
            cuvant_devirusat = cuvant
        else:
            cuvant_devirusat = cuvant[len(cuvant) - 1] + cuvant[1:len(cuvant) - 1] + cuvant[0]

        lista_cuvinte_bune.append(cuvant_devirusat)

    lista_cuvinte_bune.reverse()

    string = ""
    for cuvant in lista_cuvinte_bune:
        string += cuvant
        string += " "

    return string

#b)
def primalitate(nr):
    nr_div = 0

    if nr == 1:
        return False
    else:
        for i in range(1, nr + 1):
            if nr % i == 0:
                nr_div += 1

        if nr_div == 2:
            return True
        else:
            return False



def prime(n, numar_maxim=0):

    lista_prime = []

    for i in range(1, n):
        if primalitate(i) == True:
            lista_prime.append(i)


    if(numar_maxim == 0):
        return lista_prime
    else:
        lista_de_afisat = []
        for i in range(0, numar_maxim):
            lista_de_afisat.append(lista_prime[i])

        return lista_de_afisat


# c)

intrare = open("intrare.in", "r")
intrare_devirusata = open("intrare_devirusata.out", "w")

string = intrare.read().split('\n')

numar_propozitii = len(string)
lista_prime = prime(numar_propozitii)

if primalitate(numar_propozitii) == True:
    lista_prime.append(numar_propozitii)

contor = 1
string_de_scris = ""

for propozitie in string:
    string_de_scris = ""
    if contor in lista_prime:
        string_de_scris = deviruseaza(propozitie)
        string_de_scris += '\n'
        intrare_devirusata.write(string_de_scris)
    else:
        propozitie += '\n'
        intrare_devirusata.write(propozitie)
    
    contor += 1




      