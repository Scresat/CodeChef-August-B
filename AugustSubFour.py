def program():
    n = int(input())
    z = [int(i) for i in input().split()]

    for i in range(n-1):
        z = i % 100000007
        print(2**(n-i-1), end = ' ')
    print(1)



if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        program()