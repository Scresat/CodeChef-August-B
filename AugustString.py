def callProgram():
    big = input()
    smol = input()

    bigList = [i for i in big]
    smolList = [i for i in smol]

    bigList.sort()
    k = 0
    for i in smolList:
        bigList.remove(i)
    
    s = ''
    inserted = 0
    for i in range(len(bigList)-1):
        if ord(bigList[i]) >= ord(smolList[0]) and ord(smolList[len(smolList)-1]) < ord(bigList[i+1]) and inserted == 0:
            s+=bigList[i]  
            inserted = 1
            s += smol
        else:
            s += bigList[i] 

    if inserted == 0:
        if bigList[len(bigList)-1] > smolList[0]:
            s += smol
            s += bigList[len(bigList)-1] 
        else:
            s += bigList[len(bigList)-1] 
            s+=smol
    print(s)

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        callProgram()