def program():
    n, k = [int(i) for i in input().split()] 
    position = [int(i) for i in input().split()]
    position.sort()
    curMin = -1
    for i in range(n-1, -1, -1):
        if position[i] < k:
            if k % position[i] == 0:
                curMin = position[i]
                break 
    if curMin == -1:
        print(-1)
    else:
        print(curMin)
        



if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        program()