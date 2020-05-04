from collections import defaultdict
l = list(map(int,input().split()))
n = l[0]
m = l[1]
A = []
for i in range(int(n)):
    s = input()
    A.append(s)
B = []
for i in range(int(m)):
    s = input()
    B.append(s)
    
d = {}
for i in B:
    d[i] = []
    for j in range(n):
        if i == A[j]:
            d[i].append(j+1)
    if len(d[i]) == 0:
        d[i].append(-1)

for i in B:
    print(*d[i])
