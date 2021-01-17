"""
There are n applicants and m free apartments. 
Your task is to distribute the apartments so that as many applicants as possible will get an apartment.

Each applicant has a desired apartment size, 
and they will accept any apartment whose size is close enough to the desired size.

Input

The first input line has three integers n, m, and 
k: the number of applicants, the number of apartments, and the maximum allowed difference.

The next line contains n integers a1,a2,…,an: the desired apartment size of each applicant. 
If the desired size of an applicant is x, 
he or she will accept any apartment whose size is between x−k and x+k.

The last line contains m integers b1,b2,…,bm: the size of each apartment.

4 3 5
60 45 80 60
30 60 75

Out: 2
"""

# -- citire

numbers = [int(x) for x in input().split()]
(n, m, k) = (numbers[0], numbers[1], numbers[2])
applicants = input().split()
applicants = [int(x) for x in applicants]
sizes = input().split()
sizes = [int(x) for x in sizes]

ans = 0

# # Cum decid sa o fac? Sa vad daca iese cand sortez crescator
# applicants = sorted(applicants)
# sizes = sorted(sizes)

# for applicant in applicants:
#     if applicant in sizes:
#         ans += 1
#         sizes.pop(sizes.index(applicant))
#     else:
#         p1 = applicant - k
#         p2 = applicant + k

#         while p1 <= p2:
#             if p1 in sizes:
#                 sizes.pop(sizes.index(p1))
#                 break
            
#             elif p2 in sizes:
#                 sizes.pop(sizes.index(p2))
#                 break

#             p1 += 1
#             p2 -= 1

# print(m - len(sizes))


applicants = sorted(applicants)
sizes = sorted(sizes)

i,j,c = 0,0,0

while i < n and j < m:
    if applicants[i] + k < sizes[j]:
        i += 1
    elif applicants[i] - k > sizes[j]:
        j += 1
    else:
        i += 1
        j += 1
        c += 1

print(c)





