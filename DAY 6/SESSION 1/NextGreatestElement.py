nums=[13,7,6,12]
def GreatNums(nums):
    stack=[]
    for i in range(len(nums)):
        while stack and nums[stack[-1]]<nums[i]:
            nums[stack.pop()]=nums[i]
        stack.append(i)
    while stack:
        nums[stack.pop()]=-1
    return nums
print(GreatNums(nums))