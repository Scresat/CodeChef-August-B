import operator as op
from functools import reduce

def partitions_dp(n, d, depth=0):
    import itertools
    boxes = d
    balls = n
    rng = list(range(balls + 1)) * boxes
    return [list(i) for i in itertools.permutations(rng, boxes) if sum(i) == balls]




def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom


def program():
    n, c, k = [int(i) for i in input().split()]
    lines = {}
    for i in range(n):
        a, b, ci = [int(i) for i in input().split()]
        if ci not in lines.keys():
            lines[ci] = [[a, b]]
        else:
            lines[ci].append([a, b])

    v = [int(i) for i in input().split()]
    vi = v[0]

    triangles = {}
    for i in lines.keys():
	    triangles[i] = ncr(len(lines[i]), 3)
	

    min = sum(triangles.values())

    totalCanRemove = k // vi
    n = totalCanRemove
    d = len(lines.keys())
    part = partitions_dp(n, d)
    
    for i in range(len(part)):
        curSum = 0
        for j in range(len(part[i])):
            if len(lines[j+1])-part[i][j] >= 0:
                curSum += ncr(len(lines[j+1]) - part[i][j], 3)
        if curSum < min:
            min = curSum 
    
    print(min)


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        program()
