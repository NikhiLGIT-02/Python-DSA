def decodeWays(str):
    if not str or str[0] =='0':
        return 0
    n=len(str)
    dp=[0]*(n+1)

    #Base cases
    dp[0]=1
    dp[1]=1
    for i in range(2,n+1):
        #Single digit
        one_digit = int(str[i-1:i])        

        if 1<=one_digit<=9:
            dp[i]=dp[i]+dp[i-1]

        #Two Digits
        two_digit = int(str[i-2:1])

        if 10<=two_digit<=26:
            dp[i]=dp[i]+dp[i-2]

    return dp[n]


#Sample inputs
print(decodeWays("12"))