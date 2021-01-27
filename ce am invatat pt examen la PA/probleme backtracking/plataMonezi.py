"""
Aveti la dispozitie n saculeti cu monede, fiecare saculet continand monede de aceeasi valoare.
Sa se afiseze toate posibilitatile de a plati o suma data S folosind dnumai monede de saculeti
"""

n = int(input())
S = int(input())
V = [int(x) for x in input().split()]
M = [int(x) for x in input().split()]
P = [0] * n
Sum = 0
nrSol = 0

def afis():
    global nrSol
    nrSol += 1
    print("solutia nr ", nrSol)
    for i in range(n):
        if P[i]:
            print(P[i], " monede cu valoarea ", V[i])

def bkt(k, n):
    # cand apelam bkt(k, n) am selectat deja monede din bkt(k - 1, n) etc
    global Sum
    if k == n:
        if Sum == S:
            afis()
    else:
        # mai selectam monede din saculeti
        j = 0
        while j <= M[k] and Sum + j * V[k] <= S:
            P[k] = j
            # adaug valoarea monedelor selectate din saculetul k la valoarea totala a monedelor selectate
            Sum += j*V[k]
            bkt(k + 1, n)
            Sum -= j * V[k]
            # restaurez dupa apel valoarea variabilei globale Sum


