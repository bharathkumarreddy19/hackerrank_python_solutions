from operator import itemgetter
N, M = map(int, input().split())

lst = [[int(i) for i in input().split()] for _ in range(N)]

for i in sorted(lst, key=itemgetter(int(input()))):
    print(*i)
