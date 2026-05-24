def logisticsRoute(routes):
    
    if not routes:
        print("Please Enter the values: ")
        return
    shortest=routes[0][2]
    longest=routes[0][2]
    total=0
    city_connection = {}
    for src,dest,distance in routes:
        if distance<shortest:
            shortest=distance
        if distance>longest:
            longest=distance
        total+=distance

        city_connection[src]=city_connection.get(src,0)+1
        city_connection[dest]=city_connection.get(dest,0)+1

    average=total/len(routes)
    above_avg=0

    for src,dest,distance in routes:
        if distance>average:
            above_avg+=1
        
    print("Shortes: ",shortest)
    print("Longest: ",longest)
    print("Total: ",total)
    print("Average: ",average)
    print("Above Average: ",above_avg)
    print("City Connections: ",city_connection)

#Main
routes=[(0,1,10),(0,2,25),(1,2,15),(1,3,30),(2,3,20)]
print("TEST CASE 1")
logisticsRoute(routes)
