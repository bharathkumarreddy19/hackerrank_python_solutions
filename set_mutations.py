n = int(input())
A = set(map(int, input().split()))
for i in range(int(input())):
    op_name,len_B = input().split()
    B = list(map(int, input().split()))
    eval('A.{0}(B)'.format(op_name))
    
print(sum(A))
