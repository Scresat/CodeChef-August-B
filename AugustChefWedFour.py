if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        n, k_cost = [int(i) for i in input().split()]
        fa = [int(i) for i in input().split()]
        latn = [[0]*len(fa) for j in range(len(fa))]

        for i in range(n):
            z = {}
            for j in range(i, n, 1):
                if j == 0:
                    latn[i][j] = 0
                else:
                    latn[i][j] = latn[i][j-1] 

                if fa[j] in z:
                    if z[fa[j]] == 1:
                        latn[i][j] += 2
                    else:
                        latn[i][j] += 1
                else:
                    z[fa[j]] = 0
                
                z[fa[j]]+=1

        cur = 1000000000000000000000
        dplis = [[0]*(1001) for i in range(101)]

        for i in range(2,n+1, 1):
            dplis[1][i] = latn[0][i-1]
            
        for i in range(2, 101, 1):
            for j in range(2, n+1, 1):
                curB = 10000000000000000000
                for k in range(1, j, 1):
                    curB = min(curB, dplis[i-1][k] + latn[k][j-1]) 
                dplis[i][j] = curB
        for i in range(100):
            cur = min((i+1)*k_cost + dplis[i+1][n], cur)
        print(cur)