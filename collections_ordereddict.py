from collections import OrderedDict
D = OrderedDict()
N = input()
for i in range(int(N)):
    l = list(input().split())
    value = int(l[-1])
    name = " ".join(l[:len(l)-1])
    if name not in D.keys():
        D[name] = value
    else: 
        D[name] = D[name] + value
for n,v in D.items():
    print(n,v)
