# Linked List code

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None
    
    
    
    def insert_at_end(self,data):
        
        if(self.head == None):
            node = Node(data)
            self.head = node
        
        else:
            
            temp = self.head
            while(temp.next):
                temp = temp.next
            
            temp.next = Node(data)
            
            
        
    
    
    # def delete(self,data):
        
    
    
    def printlinkedlist(self):
        
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
        
        
        
ll = LinkedList()  
ll.insert(10)
ll.insert(12)
ll.insert(14)
ll.printlinkedlist()
    
    
    
