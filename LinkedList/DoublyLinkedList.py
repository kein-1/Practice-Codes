
class Node:
    #defines data, nextNode, and prevNode members in each Node class
    def __init__(self,data):
        self.data = data
        self.nextNode = None
        self.prevNode = None

class LinkedList:

    size = 1
    def __init__(self):
        self.head = None
        self.tail = None
    
    def getHead(self):
        return self.head

    def getTail(self):
        return self.tail
    
    def addNodeEnd(self,data):
        if (self.head == None):
            self.head = Node(data)
            return
        
        temp = self.head
        while (temp.nextNode != None):
            temp = temp.nextNode
        
        #Create the new Node. Set the current temp node's next pointer to newNode
        #Set tail to this current new node (same as temp.nextNode = newNode since temp.nextNode is the most recent node)
        #Set its previous pointer to point to the previous node 
        newNode = Node(data)
        temp.nextNode = newNode
        self.tail = temp.nextNode
        newNode.prevNode = temp   
        self.size+=1
        return


    def printListIterativelyForward(self):
        temp = self.head
        while(temp):
            print(f"Current node is: {temp.data}")
            temp = temp.nextNode
        return

    def printListIterativelyReverse(self):
        temp = self.tail
        while(temp):
            print(f"Current node is: {temp.data}")
            temp = temp.prevNode
        return


def main():
    
    llist1 = LinkedList()
    llist1.addNodeEnd(1)
    llist1.addNodeEnd(2)
    llist1.addNodeEnd(3)
    
    llist1.printListIterativelyForward()
    print(f"Current head node data is: {llist1.getHead().data}")
    print(f"Current tail node data is: {llist1.getTail().data}")
    print(f"Current size of linked list is: {llist1.size}")
    print("\n")
    llist1.printListIterativelyReverse()

if __name__=="__main__":
    main()