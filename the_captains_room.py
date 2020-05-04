k = int(input())

roomnum = list(map(int, input().split()))

s = set(roomnum)

sum_tot = sum(s) * k - sum(roomnum)

print(sum_tot // (k-1))
