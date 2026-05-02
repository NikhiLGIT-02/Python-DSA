def is_valid(s):
    stack=[]
    map={')':'(',
         '}':'{',
         ']':'['}
    for ch in s:
        if ch in map:    #Closing bracket
            top=stack.pop() if stack else '#'
            if map[ch]!=top:
                return False
        else:
            stack.append(ch)
    return not stack


print(is_valid("{(}"))