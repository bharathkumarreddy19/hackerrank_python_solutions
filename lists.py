if __name__ == '__main__':
    N = int(input())
    L = []
    for i in range(N):
        x = input().split(" ")
        command = x[0]
        if command == "insert":
            L.insert(int(x[1]),int(x[2]))
        if command == "remove":
            L.remove(int(x[1]))
        if command == "append":
            L.append(int(x[1]))
        if command == "sort":
            L.sort()
        if command == "pop":
            if (len(L) != 0):
                L.pop()
        if command == "reverse":
            L.reverse()
        if command == "print":
            print(L)
