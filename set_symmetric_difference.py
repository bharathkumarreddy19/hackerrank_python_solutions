n = int(input())
eng = set(input().split())
m = int(input())
french = set(input().split())

a = eng.symmetric_difference(french)
print(len(a))
