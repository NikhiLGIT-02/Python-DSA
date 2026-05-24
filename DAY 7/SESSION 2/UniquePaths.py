#For right and down

def unique_paths(m,n):
    #Creating 2D Dp
    dp=[[0 for _ in range(n) ]for _ in range(m)]

    #First row
    for i in range(n):
        dp[0][i]=1
    #first column
    for i in range(m):
        dp[i][0]=1
    #For remaining cells
    for i in range(1,m):
        for j in range(1,n):
            if
            #Top             #left
            dp[i][j]=dp[i-1][j]+dp[i][j-1]
    

    return dp[m-1][n-1]



#Sample inputs
m=3
n=2


print(unique_paths(m,n))