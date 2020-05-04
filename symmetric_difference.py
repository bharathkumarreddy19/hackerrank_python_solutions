m = int(input())
M = set(map(int, input().split()))
n = int(input())
N = set(map(int, input().split()))

u = M.union(N)
i = M.intersection(N)
sd = u.difference(i)
l = sorted(sd)

for k in range(len(l)):
    print(l[k])
