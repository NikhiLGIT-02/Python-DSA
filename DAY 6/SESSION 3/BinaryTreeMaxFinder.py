class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None  


class BinaryTree:
    def __init__(self):   
        self.root=None
    
    def insertNode(self,data):
        self.root=self.insert(self.root,data)

    def insert(self,root,data):
        if root is None:
            return Node(data)

        if data <=root.data:
            root.left=self.insert(root.left,data)

        else:   
            root.right=self.insert(root.right,data)

        return root
    
#Finding of Maximum element in the tree
#DFS using
#BFS Queue

    def findTheMaximum(self):
        if self.root is None:
            return float('-inf')
        return self.findMax(self.root)   
    def findMax(self,root):
        if root is None:
            return float('-inf') 
        
        leftMax=self.findMax(root.left)
        rightMax=self.findMax(root.right)

        return max(root.data, leftMax, rightMax)  
    

#Main
tree=BinaryTree()
n=int(input('Enter the number of Sections: '))
for i in range(n):
    value=int(input("Enter the values: "))
    tree.insertNode(value)

print("Maximum item quantity: ",tree.findTheMaximum())