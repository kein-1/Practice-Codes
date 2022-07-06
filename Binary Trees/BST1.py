class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            return
        temp = self.head
        
        while True:
            if temp.value > data:
                if temp.left == None:
                    temp.left = newNode
                    return
                else:
                    temp = temp.left
            else:
                if temp.right== None:
                    temp.right = newNode
                    return
                else:
                    temp = temp.right

    def searchValueIteratively(self,data):
        
        temp = self.head
        while temp:
            if temp.value == data:
                return True
            elif temp.value > data:
                temp = temp.left
            else:
                temp = temp.right
        return False

    
    def deleteNodeIteratively(self,data):
        pass

def insertRecursively(root,data):

    if not root:
        newNode = Node(data)
        root = newNode
        return root
    
    # Less than, so go left. This makes sense becuase what should the function call
    # return? It returns a node. So the base condition we are returning the address
    # of the new node. We are setting each node's left or right pointer to whatever we return 
    # from the function call, which inputs the left node's data. ]
    # If left is NULL, then we basically set root.left to the newNode made in the base case  
    elif root.value > data:
        root.left = insertRecursively(root.left,data)
    #Greater than, so go right
    else:
        root.right = insertRecursively(root.right,data)
    return root


# Search recursively by passing in the root node. Return true if found 
def searchValueRecursively(root,data):
    
    if not root:
        return False
    if root.value == data:
        return True
    elif root.value > data:
        print(root.value)
        return searchValueRecursively(root.left,data)
    else:
        print(root.value)
        return searchValueRecursively(root.right,data)


def findMaxHeight(root):

    if not root:
        return -1
    leftHeight = findMaxHeight(root.left)
    rightHeight = findMaxHeight(root.right)
    
    return 1 + max(leftHeight,rightHeight)
    

def DFSPreOrder(root):
    
    if not root:
        return
    print(root.value)
    DFSPreOrder(root.left)
    DFSPreOrder(root.right)
    return
    
def DFSInOrder(root):
    
    if not root:
        return
    DFSInOrder(root.left)
    print(root.value)
    DFSInOrder(root.right)
    
    
def DFSPostOrder(root):
    
    if not root:
        return
    DFSInOrder(root.left)
    DFSInOrder(root.right)
    print(root.value)

def main():
    
    rootNode = BST()
    rootNode.head = insertRecursively(rootNode.head,10)
    rootNode.head = insertRecursively(rootNode.head,7)
    rootNode.head = insertRecursively(rootNode.head,15)
    rootNode.head = insertRecursively(rootNode.head,4)
    rootNode.head = insertRecursively(rootNode.head,9)
    rootNode.head = insertRecursively(rootNode.head,12)
    rootNode.head = insertRecursively(rootNode.head,18)
    rootNode.head = insertRecursively(rootNode.head,3)
    # rootNode.BFS()
    # print(rootNode.findMinIteratively())
    # print(rootNode.findMaxIteratively())
    #print(findMaxHeight(rootNode.head))
    # DFSPreOrder(rootNode.head)
    DFSInOrder(rootNode.head)

if __name__ == "__main__":
   main()

