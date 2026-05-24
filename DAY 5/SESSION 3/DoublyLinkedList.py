class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def insertEnd(self,data):
        newNode=Node(data)

        if self.head is None:
            self.head=newNode
            return

        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=newNode
        newNode.prev=temp

    def displayBackWards(self):
        temp=self.head

        while temp.next:
            temp=temp.next
        while temp:
            if temp.prev:
                print(temp.data,end=" -> ")
            else:
                print(temp.data)
            temp=temp.prev

subjects=['CPP','DATA STRUCTURES','ALGORITHMS']
dll=DoublyLinkedList()

for book in subjects:
    dll.insertEnd(book)
print("The backward printing: ")
dll.displayBackWards()
