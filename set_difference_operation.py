a = int(input())
eng = set(input().split())
b = int(input())
french = set(input().split())

s = eng.difference(french)
print(len(s))
