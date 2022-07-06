
class Node:

    def __init__(self,data):
        self.data = data
        self.nextNode = None
    
class CircularLinkedList:

    def __init__(self):
        self.head = None;
    
    def addNodeEnd(self, data):
        if self.head == None:
            print("THIS RAN")
            self.head = Node(data)
            return
        temp = self.head
        
        if (temp.nextNode == None):
            newNode = Node(data)
            temp.nextNode = newNode
            newNode.nextNode = self.head 
            return
        else:
            while (temp.nextNode != self.head):
                temp = temp.nextNode
            
            newNode = Node(data)
            temp.nextNode = newNode
            newNode.nextNode = self.head

    
    def printList(self):
        temp = self.head
        while(temp != None):
            print(f"Current Node value is: {temp.data}")
            temp = temp.nextNode
            if (temp.nextNode == self.head):
                print(f"Current Node value is: {temp.data}")
                break
        
        return


def main():

    CCList1 = CircularLinkedList()
    CCList1.addNodeEnd(1)
    CCList1.addNodeEnd(2)
    CCList1.addNodeEnd(3)
    CCList1.addNodeEnd(4)
    CCList1.addNodeEnd(5)
    CCList1.printList()

if __name__=="__main__":
    main();



