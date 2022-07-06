
#Recursion methods on linkedlist 

class Node:
    def __init__(self,data):
        self.data = data
        self.nextNode = None


class LinkedList:

    size = 0

    def __init__(self):
        self.head = None

    def addNodeEnd(self, data):
        if self.head == None:
            newNode = Node(data)
            print(f"Current head id before change is is: {id(self.head)}, {id(newNode)}")
            self.head = newNode
            print(f"Current head id after change is is: {id(self.head)}, {id(newNode)}")

            return
        temp = self.head
        while (temp.nextNode != None):
            temp = temp.nextNode
        temp.nextNode = Node(data)
        self.size +=1
    
    #Very easy. Just move the head node pointer to the next node
    def deleteFrontNode(self):
        if (self.head == None):
            print("EMPTY LIST")
            return
        self.head = self.head.nextNode
        return

    #Function to Test pass by value vs pass by reference.. what is actually changing? 
    def printList(self):    
        temp = self.head
        print(id(temp), id(self.head))
        while temp != None:
            print(f"{temp.data} -> ", end = "")
            
            temp = temp.nextNode
        print("END")

    def printRecursively(self, head):
        if (head == None):
            print("END")
            return
        print(f"{head.data} -> ", end ="")
        self.printRecursively(head.nextNode)

    #NO IDEA WHY THIS DOESN'T WORK. I DON"T KNOW HOW TO IMPLEMENT RECURSION IN PYTHON CLASSES. 
    #I CAN DO IT OUTSIDE THE CLASS
    # def addNodeEndRecursivelyMETHOD(self,data):
    #     if (self.head == None):
    #         newNode = Node(data)
    #         self.head = newNode
    #         return 
    #     if (self.head.nextNode == None):
    #         newNode = Node(data)
    #         self.head.nextNode = newNode
    #         return 

    #     self.addNodeEndRecursivelyMETHOD(data)



#This works!!! I am passing in the head of the linked list. 
#Recursively call the function until we get to the last node, then Insert. Return type is void 
#Not sure why if we have an empty list, the base-condition does not work
def addNodeEndRecursively(llist,data):
    if (llist == None):
        newNode = Node(data)
        llist =  newNode
        return 
    if (llist.nextNode == None):
        newNode = Node(data)
        llist.nextNode = newNode
        
        return 

    addNodeEndRecursively(llist.nextNode,data)


#Add node end recursively with returning head:
def addNodeEndRecursively2(llist,data):

    # This is also another base coindition method: we just add the node here and return our previous node. Here
    # This base condition is sort of like the iterative condition. We stop when we find the last node rather than going 
    # past it. This method can also be applied in trees  
    if (llist.nextNode == None):
        newNode = Node(data)
        llist.nextNode = newNode
        return llist.nextNode
    
    # This method returns the node at the end. Here, llist is NONE because we pass in the last node's next address  
    # if (llist == None):
    #     return newNode(data)

    else:
        #This is saying each function call's next node value is equal to the return value of function call. 
        llist.next = addNodeEndRecursively(llist.nextNode,data)
    return llist


#How did I figure out the base condition? Every time we decrease position, we are moving to the next node
#We want to insert it at some position so we want to stop at the node BEFORE that position
#This is why i set base condition to position = 1
def addNodeMiddleRecursively(llist,data,position):
    
    if (position == 1):
        newNode = Node(data)
        newNode.nextNode = llist.nextNode
        llist.nextNode = newNode
        return
    position = position-1
    addNodeMiddleRecursively(llist.nextNode,data,position)

#Only need the head. Removes the last node recursively
#So we just need to stop at the node right before the last node. That will be our base condition
def deleteNodeEndRecursively(llist):

    if (llist.nextNode.nextNode == None):
        llist.nextNode = None
        return
    deleteNodeEndRecursively(llist.nextNode)



def main():

    LList1 = LinkedList()
    #print(f"The linked list is at : {id(LList1)}, while its head node member is at:  {id(LList1.head)}")

    LList1.addNodeEnd(1)
    #print(f"The linked list is at : {id(LList1)}, while its head node member is at:  {id(LList1.head)}")
    

    LList1.addNodeEnd(2)
    LList1.addNodeEnd(3)
    # LList1.addNodeEnd(4)
    # LList1.addNodeEnd(5)

    # LList1.printList()
    # LList1.printRecursively(LList1.head)
    print(id(LList1.head))
    LList1.head = addNodeEndRecursively2(LList1.head,4)
    print(id(LList1.head))
    # addNodeEndRecursively(LList1.head,6)
    # addNodeMiddleRecursively(LList1.head,10,3)
    print(id(LList1.head))
    LList1.printRecursively(LList1.head)
    # print("\n")
    # deleteNodeEndRecursively(LList1.head)
    # LList1.printRecursively(LList1.head)
    # LList1.deleteFrontNode()
    # print("\n")
    # LList1.printRecursively(LList1.head)

if __name__=="__main__":
    main()