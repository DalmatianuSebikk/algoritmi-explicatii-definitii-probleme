# verificarea in lista daca toate elementele sunt unice folosind liste in python

lista = [1, 20, 30, 44, 5, 56, 57, 19, 8, 9, 10, 31, 12, 13, 14, 35, 16, 27, 58, 19, 21]
ok = True
frecventa = {}

for numar in lista:
    if numar not in frecventa:
        frecventa[numar] = True
    else:
        ok = False

if ok == True:
    print("DA")
else:
    print("NU")


