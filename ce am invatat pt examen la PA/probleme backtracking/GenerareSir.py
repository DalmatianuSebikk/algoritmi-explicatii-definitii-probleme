"""
Se citesc de la tastatura numerele naturale n si lg.
Sa se afiseze toate sirurile de lg numere strict pozitive, siruri cu proprietatea ca incep si se termina
cu n, iar intre doua elemente consecutive ale sirului diferenta este exact 1.
Daca nu exista nicio solutie, se va afisa un mesaj.
pt n = 2, lg = 5 se vor afisa solutiile:
2 3 4 2
2 3 2 3 2
2 3 2 1 2
2 1 2 3 2
2 1 2 1 2
"""

n = int(input())
lg = int(input())
s = [0] * lg

# generam toate solutiile si le alegem in afis()
def bkt(k, lg):
    if k == lg:
        afis()
    else:
        if s[k - 1] > 1:
            s[k] = s[k - 1] - 1
            bkt(k + 1)
        s[k] = s[k - 1] + 1