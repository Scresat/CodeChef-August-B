def callProgram():
    h, p = [float(i) for i in input().split()]
    afterAlltheEnd = 2*p 
    if h - afterAlltheEnd <= 0:
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        callProgram()