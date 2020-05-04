import collections 

s = sorted(input().strip())


count = collections.Counter(s).most_common()
count = sorted(count, key= lambda x : (-1 * x[1],x[0]))
for x in range(3):
    print(count[x][0], count[x][1])
