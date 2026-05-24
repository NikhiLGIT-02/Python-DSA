from queue import Queue

def AverageQueue(q):
    total_items=0
    count=0

    while not q.empty():
        total_items+=q.get()
        count+=1

    if count==0:
        return 0
    avg=total_items/count
    return avg

size=int(input("Enter the size of the queue: "))
q=Queue()
print("Enter the elements of the queue: ")
for _ in range(size):
    item=int(input())
    q.put(item)

avg=AverageQueue(q)
print(f"Average Number of Items: {avg:.5f}")