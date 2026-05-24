def uniquePathsWithWall(grid):
    m=len(grid)
    n=len(grid[0])

    #start is blocked

    if grid[0][0]==1:
        return 0
    
    #Create Dp Table
    dp=[[0 for _ in range(n)]for _ in range(m)]
    dp[0][0]=1

    for i in range(m):
        for j in range(n):
            if grid[i][j]==1:
                dp[i][j]=0
            else:
                if i>0:
                    dp[i][j]=dp[i][j]+dp[i-1][j]
                if j>0:
                    dp[i][j]=dp[i][j]+dp[i][j-1]
    return dp[m-1][n-1]




grid=[[0,0,0],
     [0,1,0],
     [0,0,0]]
print(uniquePathsWithWall(grid))