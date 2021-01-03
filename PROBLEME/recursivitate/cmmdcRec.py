# cel mai mare divizor comun recursiv

# varianta iterativa
"""
def cmmdc(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

print(cmmdc(14, 21))
"""

# varianta recursiva
def cmmdc(a, b):
    if b == 0:
        return a
    else:
        return cmmdc(b, a % b)

print(cmmdc(8, 12))