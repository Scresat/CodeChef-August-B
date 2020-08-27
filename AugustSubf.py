from itertools import combinations
from collections import Counter

def program():
    n = int(input()) 
    numberList = [i for i in input().split()]
    subl = []
    for i in range(1, len(numberList)+1):
        temp = [list(x) for x in combinations(numberList, i)]
        if len(temp)>0:
            subl.extend(temp)
    print(subl)
    dictCount = {}
    for i in range(1, n+1, 1):
        dictCount[str(i)] = 0

    for i in range(len(subl)):
        c = Counter(subl[i])
        a = c.most_common(1)[0][0]
        dictCount[str(a)] += 1
        
    s = ''
    for i in range(1, n, 1):
        s+=str(dictCount[str(i)]) +' '

    s+=str(dictCount[str(n)])
    print(s)

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        program()