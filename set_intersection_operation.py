m = int(input())
eng = set(input().split())
n = int(input())
french = set(input().split())

s = eng.intersection(french)
print(len(s)) 
