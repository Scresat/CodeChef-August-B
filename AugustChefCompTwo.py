
    

def program():
    no_cities = int(input())
    edges = [] 
    for i in range(no_cities-1):
        edges.append([int(i)-1 for i in input().split()])

    P_ = [int(i)-1 for i in input().split()]
    A_ = [int(i) for i in input().split()]
    F_ = [int(i) for i in input().split()]

    endDate = []
    for i in range(len(P_)):
        endDate.append(0)


    connected = []
    for i in range(len(P_)):
        z = []
        for j in range(len(edges)):
            if i == edges[j][0]:
                z.append(edges[j][1])
            elif i == edges[j][1]:
                z.append(edges[j][0])
        connected.append(z)


    removed = []
    for i in range(len(P_)):
        visited = [] 
        fromCity=P_[i]
        population=A_[P_[i]]

        while len(visited)+1 <= len(connected[P_[i]]):
            #visitEveryone(fromCitychanged everytime, population defined at iteratoin, no need, edges no need, visited same, but change, F_ same, endDate same, originalCity P_[i], day = i, removed same, connected same):
            for i in range(len(connected[fromCity])):
                if connected[fromCity][i] not in visited and connected[fromCity][i] not in removed:
                    hereNow = connected[fromCity][i] 
                    visited.append(hereNow)
                    #print("NOW IN CITY " + str(fromCity+1) + ' FROM CITY ' + str(originalCity+1))
                    #print()
                    if F_[hereNow] != 0:
                        F_[hereNow] = F_[hereNow] - min(population, F_[hereNow]) 
                        if F_[hereNow] == 0:
                            endDate[hereNow] = i
                    #print('CONNECTED ARE ' + str([i+1 for i in connected[fromCity]]))
                    #print(F_)
            fromCity = connected[fromCity][len(visited)-1]

        removed.append(P_[i])
    

    for i in range(len(F_)):
        if F_[i] != 0:
            endDate[i] = -1

    s = ''
    for i in range(len(endDate)):
        if endDate[i] != -1:
            s += str(endDate[i]+1) + ' '
        else:
            s += str(endDate[i]) + ' '
    
    print(s.strip())



if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        program()