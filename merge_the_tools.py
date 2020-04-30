import textwrap
def merge_the_tools(string, k):
    arr = textwrap.wrap(string,k)
    for i in arr:
        temp = []
        for j in i:
            if j not in temp:
                temp.append(j)
        print(''.join(temp))
    


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
