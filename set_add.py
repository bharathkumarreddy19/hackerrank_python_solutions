N = int(input())

country = []
for i in range(N):
    country.append(input())

s = set(country)

print(len(s))
