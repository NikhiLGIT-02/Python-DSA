def fixed_size_window(arr,k):
    window_sum=sum(arr[0:k])
    maxSumAnswer=window_sum

    for right in range(k,len(arr)):
        #window_sum=old_window-outgoing_element+Incoming element
        window_sum = window_sum-arr[right-k]+arr[right]
        maxSumAnswer=max(maxSumAnswer,window_sum)
    return maxSumAnswer

#Main
value=[2,1,5,1,3,2]
k=3
print(fixed_size_window(value,k))