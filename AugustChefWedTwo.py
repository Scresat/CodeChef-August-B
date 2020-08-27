from collections import Counter

def fight(current):
    vals = Counter(current)
    s = sum([i for i in vals.values() if i >= 2])
    return s

def returnMinCost(current, i, family_, k):
    if len(family_) == i:
        return fight(current) + k
    
    current.append(family_[i])
    c1 = returnMinCost(current, i+1, family_, k)
    if current != []:
        current.pop()
    c2 = returnMinCost([family_[i]], i+1, family_, k) + fight(current) + k
    m = min(c1, c2)
    return m    


def program():
    n, k = [int(i) for i in input().split()]
    family_ = [int(i) for i in input().split()]
    current = []
    answer = returnMinCost(current, 0, family_, k)
    print(answer)

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        program()