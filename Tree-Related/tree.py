class Node:
    def __init__(self,data):
        self.key = data
        self.left = None
        self.right = None
    
    def preorder(self):
        print(self.key , end = " ")
        if(self.left):
            self.left.preorder()
        if(self.right):
            self.right.preorder()

    def postorder(self):
        if(self.left):
            self.left.postorder()
        if(self.right):
            self.right.postorder()
        print(self.key , end = " ")

    def inorder(self):
        if(self.left):
            self.left.inorder()
        print(self.key , end = " ")
        if(self.right):
            self.right.inorder()

    def levelorder(self,root):
        queue = [root]
        temp = root
        while(len(queue) > 0):
            temp = queue.pop(0) 
            print(temp.key , end=" ")
            if(temp.left):
                queue.append(temp.left)
            if(temp.right):
                queue.append(temp.right)
                

## TYPES OF BINARY TREE
def IsFullBinaryTree(root):
    if(root == None):
        return True
    else:
        if((root.left == None and root.right) or (root.left and root.right==None)):
            return False
        else:
            return IsFullBinaryTree(root.left) and IsFullBinaryTree(root.right)

## DRIVER CODE
root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("PreOrder Traversal : ", end = " ")
root.preorder()

print("\nPostOrder Traversal : ", end = " ")
root.postorder()

print("\nInOrder Traversal : ", end = " ")
root.inorder()

print("\nLevelOrder Traversal : ", end = " ")
root.levelorder(root)

print("\n")
print(IsFullBinaryTree(root))
