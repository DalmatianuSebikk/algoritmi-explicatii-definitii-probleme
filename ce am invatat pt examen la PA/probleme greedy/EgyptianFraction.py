"""
Orice fractie pozitiva poate fi reprezentata ca suma de fractii cu unitate unica. O fractie este fractie unitate
daca numaratorul este 1 si numitorul este un intreg pozitiv, de exemplu 1/3 este o fractie unitate.

Se poate rezolva problema prin intermediul metodei greedy. Pentru o anumita fractie de forma "numarator/numitor"
cautam cea mai mare fractie unitate posibila, apoi apelam recurent pentru fractia initiala - fractia unitate
gasita.
"""

from math import ceil # (pentru functia de ceiling)

def fractieEgipteana(numarator, numitor):
    # facem o lista goala unde retinem numitorul, pentru ca mai apoi sa scriem elementele ca 1/numitor
    numitori = []

    # structura while functioneaza pana cand fractia devine 0 / numaratorul devine 0
    while numarator != 0:
        # preiau ceiling pentru a face cea mai mare fractie unitate
        x = ceil(numitor / numarator)

        # stochez valoarea 
        numitori.append(x)

        # update la numarator si numitor
        numarator = x * numarator - numitor
        numitor = numitor * x

        # afisare
    for i in range(len(numitori)):
        if i != len(numitori) - 1:
             print("1/{}".format(numitori[i]) + " +")
        else:
            print("1/{}".format(numitori[i]))

fractieEgipteana(2, 3)