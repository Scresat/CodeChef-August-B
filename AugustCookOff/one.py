def program():
    _, k = [int(i) for i in input().split()]
    zl = [int(i) for i in input().split()]

    zl.sort()
    cursum = zl[0]
    i = 1
    step = 0
    sigmoid = 0
    while i < len(zl):
        if cursum + zl[i] > k:
            step+=1
            
            sigmoid = i
        else:
            sigmoid = i


if __name__ == "__main__":
    for i in range(int(input())):
        program()