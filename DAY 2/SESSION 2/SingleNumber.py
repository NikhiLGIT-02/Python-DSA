def single_number(nums):
    xor=0
    for num in nums:
        xor=xor^num
    diff_bit=xor&-xor
    a=0
    b=0

    for num in nums:
        if (num and diff_bit)==0:
            a=a^num
        else:
            b=b^num
    return [a,b]

nums=[1,2,1,3,2,5]
result = single_number(nums)
print(result[0],result[1])