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

    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        self.head = prev

    def swap_nodes(self, x, y):
        if x == y:
            return

        prevX = None
        prevY = None
        currX = self.head
        currY = self.head

        # Find X
        while currX and currX.data != x:
            prevX = currX
            currX = currX.next

        # Find Y
        while currY and currY.data != y:
            prevY = currY
            currY = currY.next

        # If not found
        if not currX or not currY:
            return

        # Fix previous pointers
        if prevX:
            prevX.next = currY
        else:
            self.head = currY

        if prevY:
            prevY.next = currX
        else:
            self.head = currX

        # Swap next pointers
        temp = currX.next
        currX.next = currY.next
        currY.next = temp

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Input
n = int(input('Enter the number: '))
arr = list(map(int, input('Enter n values: ').split()))
a, b = map(int, input('Enter two values: ').split())

# Create list
sll = LinkedList()
for i in arr:
    sll.insertAtEnd(i)

# Original
sll.display()

# Reverse
sll.reverse()
sll.display()

# Swap
sll.swap_nodes(a, b)
sll.display()