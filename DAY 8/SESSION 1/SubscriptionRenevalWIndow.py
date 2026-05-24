def longest_window(days,k):
    left=0
    max_len=0

    for right in range(len(days)):
        while days[right]-days[left]>k:
            left+=1
        max_len=max(max_len,right-left+1)
    return max_len
#Main
days=[1,3,5,7,9]
k=4
print(longest_window(days,k))