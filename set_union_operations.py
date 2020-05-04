n = int(input())
r = list(map(int,input().split()))
b = int(input())
rr = list(map(int,input().split()))

eng = set(r)
french = set(rr)

union = eng.union(french)
print(len(union))
