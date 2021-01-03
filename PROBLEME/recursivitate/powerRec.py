# calculeaza recursiv un numar la o putere data

def powerRec(x, n):
    if n == 0:
        return 1
    else:
        return x * powerRec(x, n - 1)

print(powerRec(2, 3))