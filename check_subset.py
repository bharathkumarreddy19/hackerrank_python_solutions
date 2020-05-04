n = int(input())

for t in range(n):
    numA = int(input())
    eleA = set(map(int,input().split()))
    numB = int(input())
    eleB = set(map(int,input().split()))
    print(eleA.issubset(eleB))
