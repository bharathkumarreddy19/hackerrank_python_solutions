A = set(input().split())
n = int(input())
output = True
for i in range(n):
    s = set(input().split())
    if (s.issubset(A) and len(A.difference(s)) > 0) == False:
        output = False
print(output)
