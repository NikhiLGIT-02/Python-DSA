class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode
    
    def removeDupes(self):
        seen = set()
        temp = self.head
        prev = None

        while temp:
            if temp.data in seen:
                prev.next = temp.next
            else:
                seen.add(temp.data)
                prev = temp
            temp = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


# Input Section
ids = list(map(int, input('Enter the patient ID: ').split()))
sll = LinkedList()

for x in ids:
    sll.insertAtEnd(x)

sll.removeDupes()

print('Unique ids display:')
sll.display()