# conversia in binar a unui numar in baza 10

# varianta iterativa
"""
def convBinarRec(n):
    # mai bine pui intr-o lista tho
    binar = []
    while n > 0:
        binar.append(n % 2)
        n = n // 2
    
    nrbin = 0
    for i in range(len(binar) - 1, -1, -1):
        nrbin = nrbin * 10 + binar[i]

    return nrbin

print(convBinarRec(6))
"""

# varianta recursiva
# FORMULA: f(n) = n % 2 + f([n / 2]), unde [] e partea intreaga!

# EXPLICATIE:
# ai resturile pana cand n = 0. Ai ultimul rest * 10 + penultimul rest (notam cu s). apoi s * 10 + 
# antepenultimul rest, si tot asa pana ajungi la primul rest.
""" 
def convBinarRec(n):
    if n == 0:
        return 0
    else:
        return convBinarRec(n // 2) * 10 + n % 2

print(convBinarRec(6))
"""