rows=4
#Upper half
for i in range(1,rows+1):
    #Right Angled Triangle
    for j in range(i):
        print('*',end=" ")
    #Spaces in the middle
    for j in range(2*(rows-i)):
        print(" ",end=" ")
    #Mirror Image of right angled traingle
    for i in range(i):
        print('*',end=" ")
    print()

#Second half
for i in range(rows,0,-1):
    #Right Angled Triangle
    for j in range(i):
        print('*',end=" ")
    #Spaces in the middle
    for j in range(2*(rows-i)):
        print(" ",end=" ")
    #Mirror Image of right angled traingle
    for i in range(i):
        print('*',end=" ")
    print()