from itertools import combinations
from collections import Counter

def program():
    n = int(input()) 
    numberList = [i for i in input().split()]
    subl = []
    for i in range(1, pow(2,len(numberList)), 1):
        binary_array = [int(j) for j in bin(i)[2:]]
        zero_array = [0]*(len(numberList) - len(binary_array))
        binary_array_full = zero_array + binary_array
        sub_array = [numberList[k]*binary_array_full[k] for k in range(len(binary_array_full))]
        subl.append([i for i in sub_array if i != ''])

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