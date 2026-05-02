def thirdMax(nums):
    nums.sort()

    unique=[]
    unique.append(nums[0])

    for i in range(len(nums)):
        if nums[i]!=nums[i-1]:
            unique.append[nums[i]]

    k=len(unique)
    if k<3:
        return unique[k-1]
    
    #High and Low
    low=0
    high=k-1
    target=k-3
    
    while low<=high:
        #mid=low+(high-low)/2
        mid=(low+high)//2
        if mid==target:
            return unique[mid]
        elif mid<target:
            low=mid+1
        else:
            high=mid-1
    return -1



n=int(input('Enter the number n: '))
nums = list(map(int, input('Enter the numbers: ').split()))
print('Third max:',thirdMax(nums))


#l=[5,4,3,2,1,89,100,-5,76]
#l.sort()
#print(l)
#print(l[-3])