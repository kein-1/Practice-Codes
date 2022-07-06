from audioop import add


class Node:
    #defines data, nextNode, and prevNode members in each Node class
    def __init__(self,data):
        self.data = data
        self.nextNode = None

class LinkedList:

    size = 1
    def __init__(self):
        self.head = None


#Returns the head of the linkedlist. Takes in the object itself
def addNodeEnd(LList, data):

    if (LList.head == None):
        newNode = Node(1)
        LList.head = newNode
        return 
    
    temp = LList.head
    while (temp.nextNode != None):
        temp = temp.nextNode
    temp.nextNode = Node(data)

def addNodeEndRecursively(LList,data):
    print(f"THIS TYPE IS: {type(LList)}")
    if (LList.nextNode == None):
        print(LList)
        print("This ran")
        print(LList)
        LList.nextNode = Node(data)
        return 
    addNodeEndRecursively(LList.nextNode,data)




def printList(LList):    
    temp = LList.head
    while temp != None:
        print(f"{temp.data} -> ", end = "")
        
        temp = temp.nextNode
    print("END")   




def main():

    LList1 = LinkedList()
    addNodeEnd(LList1,1)
    addNodeEnd(LList1,2)
    addNodeEnd(LList1,3)
    #This recursively works 
    addNodeEndRecursively(LList1.head,4)
    addNodeEndRecursively(LList1.head,5)
    addNodeEndRecursively(LList1.head,6)
    
    printList(LList1)



if __name__=="__main__":
    main()