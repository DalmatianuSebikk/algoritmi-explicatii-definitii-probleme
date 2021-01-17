# Avem multimea de valori a = {a1, a2, a3, ...., an}. 
# Se cauta submultimea a carei suma a elementelor este maxima
# Pai vom parcurge multimrea si vom lua doar elementele pozitive.

A = [-5, 3, 2, -1, 4, 1, -9, -2, 6]
S = [] # consideram S multimea de solutii
k = 0
for i in A:
    if i > 0:
        S.append(i)
        k += 1

print(S)