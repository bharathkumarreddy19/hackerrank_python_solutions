n = int(input())
s = set(map(int, input().split()))
c = int(input())
for i in range(1,c+1):
    
    eval('s.{0}({1})'.format(*input().split()+['']))
        
print(sum(s))

