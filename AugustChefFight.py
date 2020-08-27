def callProgram():
    pc, pr = [int(i) for i in input().split()]
    zc = pc//9
    if zc*9 < pc:
        zc+=1 
    
    zr = pr//9
    if zr*9 < pr:
        zr+=1 
    
    if zc >= zr:
        print(1, zr) 
    else:
        print(0, zc)


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        callProgram()