n=int(input('Enter no. of rows: '))
r=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(r, end=" ")
        r+=1
    print()