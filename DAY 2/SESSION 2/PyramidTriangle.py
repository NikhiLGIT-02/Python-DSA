rows=5
for i in range(1,rows-1):
    for j in range(2*i-1):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()