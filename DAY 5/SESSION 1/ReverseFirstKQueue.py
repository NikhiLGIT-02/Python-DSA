from collections import deque

def reverse(queue,k):
    if not queue or k>len(queue) or k<0:
        return

    stack=[]
    for i in range(k):
        stack.append(queue.popleft())

    while stack:
        queue.append(stack.pop())

    for i in range(len(queue)-k):
        queue.append(queue.popleft())
    
    return queue

#Main
queue=deque([1,2,3,4,5])
print(reverse(queue,3))

