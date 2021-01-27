f = [0,0,0]
a = [1,1,1]

def bk(k, n):
    if n == k:
        print(a)
    else:
        for i in range(n):
            if f[i] == 0:
                f[i] = 1
                a[k] = i + 1
                bk(k + 1, n)
                f[i] = 0


bk(0, 3)