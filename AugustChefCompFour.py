n = int(input())
for i in range(n):
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
        queue = []
        queue.append(P_[i])
        

        while queue:
            currentCity = queue.pop(0)
            visited.append(currentCity)
            #print("NOW IN CITY " + str(currentCity+1) + ' FROM CITY ' + str(P_[i]+1))
            #print()
            if F_[currentCity] != 0:
                F_[currentCity] = F_[currentCity] - min(A_[P_[i]], F_[currentCity]) 
                if F_[currentCity] == 0:
                    endDate[currentCity] = i+1
            #print('CONNECTED ARE ' + str([i+1 for i in connected[currentCity]]))
            #print(F_)
            
            for z in range(len(connected[currentCity])):
                if connected[currentCity][z] not in visited and removed[connected[currentCity][z]] != -1:
                    queue.append(connected[currentCity][z])
        
        # Removing the city people from all connections
        removed[P_[i]] = -1
    #print(F_)

    for i in range(len(F_)):
        if F_[i] != 0:
            endDate[i] = -1

    s = ''
    for i in range(len(endDate)):
        s += str(endDate[i]) + ' '
    
    print(s.strip())