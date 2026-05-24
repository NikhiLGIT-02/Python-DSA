def change(amount,coins):
    dp=[0]*(amount+1)
    dp[0]=1

    #Process each coin
    for coin in coins:
        for j in range(coin,amount+1):
            dp[j]=dp[j]+dp[j-coin]
    return dp[amount]


#Drivers Code
amount=5

coins=[1,2,5]
print(change(amount,coins))