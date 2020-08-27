def visitEveryone(fromCity, population, edges, visited, F_, endDate, originalCity, day):
    if fromCity in visited:
        return

    visited.append(fromCity)
    if F_[fromCity] != 0:
        F_[fromCity] = F_[fromCity] - min(population, F_[fromCity]) 
        if F_[fromCity] == 0:
            endDate[fromCity] = day

    connected = []
    
    for i in range(len(edges)):
        if fromCity == edges[i][0]:
            connected.append(edges[i][1])
        elif fromCity == edges[i][1]:
            connected.append(edges[i][0])

    if connected == []:
        return 

    for i in range(len(connected)):
        if connected[i] not in visited:
            visitEveryone(connected[i], population, edges, visited, F_, endDate, originalCity, day)

    

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

    for i in range(len(P_)):
        visited = [] 
        visitEveryone(P_[i], A_[P_[i]], edges, visited, F_, endDate, P_[i], i)


            if fromCity in visited:
                return

            visited.append(fromCity)
            if F_[fromCity] != 0:
                F_[fromCity] = F_[fromCity] - min(population, F_[fromCity]) 
                if F_[fromCity] == 0:
                    endDate[fromCity] = day

            connected = []
            
            for i in range(len(edges)):
                if fromCity == edges[i][0]:
                    connected.append(edges[i][1])
                elif fromCity == edges[i][1]:
                    connected.append(edges[i][0])

            if connected == []:
                return 

            for i in range(len(connected)):
                if connected[i] not in visited:
                    visitEveryone(connected[i], population, edges, visited, F_, endDate, originalCity, day)




        # Removing the city people from all connections
        for k in range(len(edges)):
            if P_[i] == edges[k][0] or P_[i] == edges[k][1]:
                edges[k][0] = -1
                edges[k][1] = -1
    #print(F_)

    for i in range(len(F_)):
        if F_[i] != 0:
            endDate[i] = -1

    s = ''
    for i in range(len(endDate)):
        if endDate[i] != -1:
            s += str(endDate[i]+1) + ' '
        else:
            s += str(endDate[i])
    
    print(s)



if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        program()