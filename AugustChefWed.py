from collections import Counter

def program():
    n, k = [int(i) for i in input().split()]
    families = input().split()

    ine = 1
    for i in range(1, n, 1):
        if families[i-1] == families[i]:
            ine+=k 
        else:
            continue

    print(ine)

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        program()