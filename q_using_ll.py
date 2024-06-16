# A linked list (LL) node 
# to store a queue entry 
class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
class MyQueue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.sz=0
    
    def size(self):
        return self.sz
    
       
    
    #Function to push an element into the queue.
    def push(self, item):
        temp=Node(item)
        if self.rear==None:
            self.front=temp
        else:
            self.rear.next=temp
        self.rear=temp
        self.sz+=1
         
         #Add code here
    
    #Function to pop front element from the queue.
    def pop(self):
        if self.front==None:
            return -1
        else:
            res=self.front.data
            self.front=self.front.next
            if self.front==None:
                self.rear=None
            self.sz-=1
            return res
         
         #add code here
