def visitEveryone(fromCity, population, visited, F_, endDate, originalCity, day, edges):
    visited.append(fromCity)
    #print("NOW IN CITY " + str(fromCity+1) + ' FROM CITY ' + str(originalCity+1))
    #print()
    if F_[fromCity] != 0:
        F_[fromCity] = F_[fromCity] - min(population, F_[fromCity]) 
        if F_[fromCity] == 0:
            endDate[fromCity] = day
            
    #print('CONNECTED ARE ' + str([i+1 for i in range(len(edges[fromCity])) if edges[fromCity][i] == 1]))
    #print(F_)
    for i in range(len(edges[fromCity])-1):
        if edges[0][i] != -1 and edges[fromCity+1][i+1] == 1 and i not in visited:
            visitEveryone(i, population, visited, F_, endDate, originalCity, day, edges)

    

def program():
    no_cities = int(input())
    edges = [ [ 0 for i in range(no_cities+1) ] for j in range(no_cities+1) ]
    for i in range(no_cities-1):
        a, b = [int(i) for i in input().split()]
        edges[a][b] = 1
        edges[b][a] = 1

    P_ = [int(i)-1 for i in input().split()]
    A_ = [int(i) for i in input().split()]
    F_ = [int(i) for i in input().split()]

    endDate = []
    for i in range(len(P_)):
        endDate.append(0)

    for i in range(len(P_)):
        visited = [] 
        visitEveryone(P_[i], A_[P_[i]], visited, F_, endDate, P_[i], i, edges)
        
        # Removing the city people from all connections
        edges[0][P_[i]] = -1
        edges[P_[i]][0] = -1

       
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