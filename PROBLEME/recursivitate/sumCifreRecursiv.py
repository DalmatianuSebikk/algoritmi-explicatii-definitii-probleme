# suma recursiva a cifrelor unui numar

def sumCifreRecursiv(n):
    if n < 10:
        return n
    else:
        return n % 10 + sumCifreRecursiv(n // 10)

print(sumCifreRecursiv(10))