n=int(input('Enter N: '))
k=int(input('Enter K: '))


nums=list(map(int,input().split()))
result=[0]*n

if k==0:
    result=[0]*n
elif k>0:
    for i in range(n):
        sum=0
        for j in range(1,k+1):
            sum+=nums[(i+j)%n]
        result[i]=sum
else:
    k=-k
    temp=[nums[i%n]for i in range(2*n)]


    prefixSum=[0]*(2*n)
    prefixSum[0]=temp[0]

    for i in range(1,2*n):
        prefixSum[i]=prefixSum[i-1]+temp[i]
    #left =0,right =0
    for i in range(n):
        left=i+n-k
        right=i+n-1

        if left==0:
            result[i]=prefixSum[right]
        else:
            result[i]=prefixSum[right]-prefixSum[left-1]
print(result)