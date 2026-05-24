class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None  


class BST:
    def __init__(self):   
        self.root=None
    
    def insert(self,root,data):
        if root is None:
            return Node(data)

        if data <=root.data:
            root.left=self.insert(root.left,data)

        else:   
            root.right=self.insert(root.right,data)

        return root
    
    def KthLargest(self,root,k):
        