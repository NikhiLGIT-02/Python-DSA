def spiral_order(matrix,m,n):
    top=0
    left=0
    bottom=m-1
    right=n-1

    while top<=bottom and left<=right:
        #First row
        for i in range(left,right+1):
            print(matrix[top][i],end=" ")
        top+=1

        #Right Column
        for i in range(top,bottom+1):
            print(matrix[i][right],end=" ")
        right-=1
        
        #Bottom row
        if top<=bottom:
            for i in range(right,left-1,-1):
                print(matrix[bottom][i],end=" ")
        bottom-=1

        if left<=right:
            for i in range(bottom,top-1,-1):
                print(matrix[i][left],end=" ")
        left+=1

#Main
m=3
n=3

matrix=[[1,2,3],[4,5,6],[7,8,9]]

print(matrix)
print(spiral_order(matrix,m,n))