
class Node:

    def __init__(self,data):
        self.data = data
        self.nextNode = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def addNodeEnd(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            return
        temp = self.head
        while (temp.nextNode != None):
            temp = temp.nextNode
        temp.nextNode = newNode

    def printList(self):
        temp = self.head
        while temp != None:
            print(f"{temp.data} -> ")
            temp = temp.nextNode


    def addNodeCirc(self,data,index):
        temp = self.head
        curr = self.head
        while temp.nextNode != None:
            temp = temp.nextNode
        
        for i in range(index):
            curr = curr.nextNode

        newNode = Node(data)
        temp.nextNode = newNode
        newNode.nextNode = curr
        
    def cycleOrNot(self):

        slow = fast = self.head
        while fast != None and fast.nextNode != None:
            fast = fast.nextNode.nextNode
            slow = slow.nextNode
            if (slow == fast):
                return True
        return False
    
    def cycleLength(self):

        slow = fast = self.head
        counter = 0
        while fast != None and fast.nextNode != None:
            fast = fast.nextNode.nextNode
            slow = slow.nextNode
            if (slow == fast):
                break
        slow = slow.nextNode
        counter+=1
        while slow is not fast:
            slow = slow.nextNode
            counter +=1
        return counter


def main():

    llist1 = LinkedList()
    llist1.addNodeEnd(1)
    llist1.addNodeEnd(2)
    llist1.addNodeEnd(3)
    llist1.addNodeEnd(4)
    llist1.addNodeEnd(5)
    llist1.addNodeCirc(6,1)
    #llist1.printList()
    print(llist1.cycleOrNot())
    #print(llist1.head.data)
    print(llist1.cycleLength())

if __name__=="__main__":
    main()



