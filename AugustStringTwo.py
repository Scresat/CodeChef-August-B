def program():
    big = input()
    smol = input()
    letter = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}

    for i in big:
        letter[i]+=1 
    
    for i in smol:
        letter[i]-=1 

    s = ''
    letterList = [i for i in letter.keys() if letter[i] != 0]
    inserted = 0
    for i in range(len(letterList)):
        if inserted == 1:
            s+=letterList[i]*letter[letterList[i]] 
        else:
            if  letterList[i] < smol[0] and inserted == 0:
                s+=letterList[i]*letter[letterList[i]] 
            elif letterList[i] == smol[0] and inserted == 0:
                after = 0
                for j in range(1, len(smol), 1):
                    if smol[j] > smol[0]:
                        after = 1
                        break
                    elif smol[j] == smol[0]:
                        continue 
                    else:
                        after = 0
                        break
                
                if after == 1:
                    s+=letterList[i]*letter[letterList[i]]
                    s+=smol
                    inserted = 1 
                else:
                    s+=smol 
                    s+=letterList[i]*letter[letterList[i]] 
                    inserted = 1

            elif letterList[i] > smol[0] and inserted == 0:
                s+=smol
                s+=letterList[i]*letter[letterList[i]]
                inserted = 1 
                
    if inserted == 0:
        s+=smol 

    print(s)
    


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        program()