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
    print(f"THIS TYPE IS: {type(LList)} and it is at {id(LList)}")
    if (LList.head == None):
        newNode = Node(1)
        print(f"{id(LList.head)} {id(newNode)}")
        LList.head = newNode
        return 
    
    temp = LList.head
    while (temp.nextNode != None):
        temp = temp.nextNode
    temp.nextNode = Node(data)

#Returns the head of the linkedlist. Takes in the object itself
# def addNodeEnd(LList, data):
#     print(f"THIS TYPE IS: {type(LList)} and it is at {id(LList)}")
#     if (LList == None):
#         newNode = Node(1)
#         LList = newNode
#         return 
    
#     temp = LList
#     while (temp.nextNode != None):
#         temp = temp.nextNode
#     temp.nextNode = Node(data)

#I can't understand WHY this doesn't work. 
def addNodeEndRecursively(LList,data):
    print(f"THIS TYPE IS: {type(LList)} and it is at {id(LList)}")

    #LList is STILL None after this
    if (LList == None):
        newNode = Node(data)
        print(f"{id(LList)} {id(newNode)}")
        LList = newNode
        return

    if (LList.nextNode == None):
        print(LList)
        LList.nextNode = Node(data)
        return
    print(f"Curr and nex ID: {id(LList)} {id(LList.nextNode)}")
    addNodeEndRecursively(LList.nextNode,data)




def printList(LList):    
    temp = LList.head
    while temp != None:
        #print(id(temp))
        print(f"{temp.data} {id(temp)}-> ", end = "")
        
        temp = temp.nextNode
    print("END")   




def main():

    LList1 = LinkedList()
    #print(f"OUTSIDE {id(LList1.head)}")
    #addNodeEnd(LList1,1)
    #print(f"OUTSIDE {id(LList1.head)}")
    #addNodeEnd(LList1,2)
    #addNodeEnd(LList1,3)
    print(f"OUTSIDE {id(LList1.head)}")
    addNodeEndRecursively(LList1.head,4)
    addNodeEndRecursively(LList1.head,5)
    #addNodeEndRecursively(LList1.head,6)
    
    printList(LList1)



if __name__=="__main__":
    main()