
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
            self.head = Node(data)
            return
        temp = self.head
        while (temp.nextNode != None):
            temp = temp.nextNode
        temp.nextNode = Node(data)
        self.size +=1
    
    # def addNodeEndRecursively(self,head):
    #     self.head 
    #     if (self.head == None):
    #         self.head = Node(data)
    #         return
    #     elif (h)

   
    #Function to Test pass by value vs pass by reference.. what is actually changing? 
    def printList(self):
        
        
        temp = self.head
        # while self.head != None:
        #     # print(f"{temp.data} -> ", end ="")
        #     # print(f"Temp id and data is at: {id(temp)} {id(temp.data)} and its value is : {temp.data} and self.head id and data is at: {id(self.head)} {id(self.head.data)} and its value is: {self.head.data}")
        #     # print(f"{temp.data} -> ", end = "")
        #     #self.head = self.head.nextNode
        #     print(f"Head curr and next: {id(self.head)} {id(self.head.nextNode)} ")
        #     print(f"Temp curr and next: {id(temp)} {id(temp.nextNode)} ")
            
        #     self.head = self.head.nextNode
        #     temp = temp.nextNode
        
        while temp != None:
            # print(f"{temp.data} -> ", end ="")
            # print(f"Temp id and data is at: {id(temp)} {id(temp.data)} and its value is : {temp.data} and self.head id and data is at: {id(self.head)} {id(self.head.data)} and its value is: {self.head.data}")
            # print(f"{temp.data} -> ", end = "")
            #self.head = self.head.nextNode
            print(f"Head curr and next: {id(self.head)} {id(self.head.nextNode)} ")
            #print(f"Temp curr and next: {id(temp)} {id(temp.nextNode)} ")
            

        print("END")

    def printRecursively(self, head):
        if (head == None):
            print("END")
            return
        print(f"{head.data} -> ", end ="")
        self.printRecursively(head.nextNode)



def main():

    LList1 = LinkedList()

    LList1.addNodeEnd(1)
    LList1.addNodeEnd(2)
    LList1.addNodeEnd(3)
    LList1.addNodeEnd(4)
    LList1.addNodeEnd(5)

    LList1.printList()
    LList1.printList()
    #LList1.printRecursively(LList1.head)
   
    #LList1.foo()



if __name__=="__main__":
    main()