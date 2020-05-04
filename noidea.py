n,m = map(int, input().split())
a = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
l = []

for num in range(len(a)):
    if a[num] in A:
        l.append(1)
    elif a[num] in B:
        l.append(-1)
    
print(sum(l))
