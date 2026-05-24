def longest_window(s):
    char_set=set()
    left=0
    right=0
    max_len=0

    for right in range(len(s)):
        current=s[right]
        while current in char_set:
            char_set.remove(s[left])
            left+=1
        char_set.add(current)
        max_len=max(max_len,right-left+1)
    return max_len




#Driver Code
s="abcabcbb"
print(longest_window(s))