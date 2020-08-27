def visitEveryone(fromCity, population, visited, F_, endDate, originalCity, day, removed, connected):
    visited.append(fromCity)
    #print("NOW IN CITY " + str(fromCity+1) + ' FROM CITY ' + str(originalCity+1))
    #print()
    if F_[fromCity] != 0:
        F_[fromCity] = F_[fromCity] - min(population, F_[fromCity]) 
        if F_[fromCity] == 0:
            endDate[fromCity] = day
    #print('CONNECTED ARE ' + str([i+1 for i in connected[fromCity]]))
    #print(F_)
    
    for i in range(len(connected[fromCity])):
        if connected[fromCity][i] not in visited and removed[connected[fromCity][i]] != -1:
            visitEveryone(connected[fromCity][i], population, visited, F_, endDate, originalCity, day, removed, connected)

    

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

    removed = []
    connected = []
    for i in range(len(P_)):
        removed.append(0)
        z = []
        for j in range(len(edges)):
            if i == edges[j][0]:
                z.append(edges[j][1])
            elif i == edges[j][1]:
                z.append(edges[j][0])
        connected.append(z)


    
    for i in range(len(P_)):
        visited = [] 
        visitEveryone(P_[i], A_[P_[i]], visited, F_, endDate, P_[i], i, removed, connected)
        
        # Removing the city people from all connections
        removed[P_[i]] = -1
    #print(F_)

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