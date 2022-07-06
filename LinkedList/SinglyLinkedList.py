#Important Python OOP notes:
#Variables do not need to be defined. We define them in constructor
#Must use self. Self is what we use to refer to the class' member
#Each method of a class must have a self parameter 




class Node:
    
    #Don't need to create the variables. Just 
    #Just define them in the constructor part 
    
    def __init__(self,data):
        self.data = data
        self.nextNode = None
        
    
class LinkedList:

    #Class variable to keep track of the size of the list 
    size = 1;
    
    #define the head and tail variable and set it to None(which is null)
    def __init__(self):
        self.head = None
        self.tail = None
        
    
    def getHead(self):
        return self.head;
    
    def getTail(self):
        return self.tail;
    
    
    #Very important: must use SELF in the class to reference the class' 
    #variable
    #In python we don't need to define the Node object. We can declare this at Node(data)
    def addNodeEnd(self, data):
        if self.head == None:
            print("THIS RAN")
            self.head = Node(data)
            return
        temp = self.head
        while (temp.nextNode != None):
            temp = temp.nextNode
        temp.nextNode = Node(data)
        self.tail = temp.nextNode
        self.size +=1
    

    # #llist here is llist.head... so basically in this function we are returning the head node that was passed in. This method is the same 
    # as using the class method i usually write. The difference here is that this is a function that takes in the head, while my method just uses self


    # def insertNodeAtPosition(llist, data, position):
    # # Write your code here
    # if (llist == None):
    #     newNode = SinglyLinkedListNode(data)
    #     llist = newNode
    #     return llist












    #If both head and tail are null, then just create the new node 
    def addNodeUsingTail(self,data):
        if self.head and self.tail == None:
            print("THIS RAN2")
            self.head = Node(data);
            self.tail = self.head;
            self.size +=1
            return
        
        self.tail.nextNode = Node(data)
        self.tail = self.tail.nextNode
        self.size +=1

    def addAfterIndex(self,index,data):
        if (self.head == None):
            print("EMPTY LIST")
            return
        elif (index < 0 or index > self.size ):
            print("Invalid index")
            return

        temp = self.head
        #Loop to the node just before the one we want to add
        for i in range(index-1):
            temp = temp.nextNode
        
        #We can create the new node simply like this
        new_Node = Node(data)

        #Now set this new node's next pointer to whatever the temp node is currently pointing to, then set temp's next node pointer
        #to point to this
        new_Node.nextNode = temp.nextNode
        temp.nextNode = new_Node
        self.size+=1
        return



    def printList(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.nextNode
            
    #method to print list recursively. Very important: for class methods
    #to call itself, we must include self.<method name> (parameters)
    def printListRecursively(self,head):
        if head == None:
            return
        print(head.data)
        #Member function so we must add self in front and we must provide return 
        return self.printListRecursively(head.nextNode)
        
    def deleteNodeEnd(self):
        
        temp = self.head;
        while temp != None:
            temp = temp.nextNode
            if (temp.nextNode.nextNode == None):
                break;
        temp.nextNode = None;
        self.tail = temp;
        self.size-=1
    
    #Deletes at a certain index
    def deleteAtIndex(self, index):
        
        if (self.head == None):
            print("EMPTY LIST")
            return
        elif (index < 0 or index > self.size ):
            print("Invalid index")
            return

        temp = self.head
        #Loop to the node just before the one we want to delete 
        for i in range(index-1):
            temp = temp.nextNode
        
        temp.nextNode = temp.nextNode.nextNode
        self.size-=1
        return
    
    
        
        
        

def main():

    llist1 = LinkedList()
    llist1.addNodeEnd(3)
    llist1.addNodeEnd(4)
    llist1.addNodeEnd(5)
    llist1.addNodeUsingTail(6)
    llist1.addNodeUsingTail(7)
    llist1.addNodeEnd(8)
    llist1.addNodeUsingTail(9)
    
    llist1.addAfterIndex(3,10)
    llist1.printList()
    print(f"The size of this list : {llist1.size}")
    llist1.printList()


if __name__=="__main__":
    main()



