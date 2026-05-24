s="55+DC"
stack=[]
for ch in s:
    if ch.isnumeric():
        stack.append(int(ch))
    elif ch=="C":
        stack.pop()
    elif ch=="D":
        stack.append(int(stack[-1]))
    elif ch=="+":
        stack.append(int(stack[-1]+int(stack[-2])))
print(stack)
print(sum(map(int,stack)))

