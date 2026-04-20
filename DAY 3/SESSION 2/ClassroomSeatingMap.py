list1=[[1,0,1],[0,0,1],[1,1,0]]

count_zero=0
count_one=0

for i in range(len(list1)):
    for j in range (i):
        if list1[i][j]==1:
            count_one+=1
        else:
            count_zero+=1

        

print('Occupied: ',count_one)
print('Empty: ',count_zero)