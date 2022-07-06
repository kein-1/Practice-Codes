
class Node():
    def __init__(self,value):
        self.data = value
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
    def addNode(self,value):
        
        newNode = Node(value)
        
        if not self.head:
            self.head = newNode
            return
        temp = self.head
        
        while temp.next != None:
            temp = temp.next
        temp.next = newNode

    
    def printList(self):
        temp = self.head
        while temp:
            print(f"Current data is: {temp.data}")
            temp = temp.next

#Must return head for some reason. Can't void function it
def addOutside(head,value):
        newNode = Node(value)
        print(id(head))
        if head == None:
            head = newNode
            print(id(head), id(newNode))
            return head
        temp = head
        
        while temp.next != None:
            temp = temp.next
        temp.next = newNode
        return head
    
def addRecursively(head,value):
        
        if head == None:
            newNode = Node(value)
            head = newNode
            return head
        head.next = addRecursively(head.next,value)
        return head
        
def addRecursively2(head,value):
        
        if head == None:
            newNode = Node(value)
            head = newNode
            return
        
        if head.next == None:
            newNode = Node(value)
            head.next = newNode
            return
        return addRecursively2(head.next,value)
            
def main():
    
    head1 = LinkedList()
    # head.addNode(1)
    # head.addNode(2)
    # head.addNode(3)
    # head.addNode(4)
    # head.addNode(5)
    # head1.head = addRecursively(head1.head,1)
    # head1.head = addRecursively(head1.head,2)
    # head1.head = addRecursively(head1.head,3)
    # head1.head = addRecursively(head1.head,4)
    # head1.head = addRecursively(head1.head,5)
    
    # addRecursively2(head1.head,1)
    # addRecursively2(head1.head,2)
    # addRecursively2(head1.head,3)
    
    head1.head = addOutside(head1.head,1)
    head1.head = addOutside(head1.head,2)
    head1.head = addOutside(head1.head,3)
    print(id(head1.head))
    head1.printList()
    
    
    
    
if __name__ == "__main__":
    main()
    