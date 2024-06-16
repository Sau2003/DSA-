#User function Template for python3

class MyQueue:
    def __init__(self):
        self.q1=[]
    
    #Function to push an element x in a queue.
    def push(self, x):
        self.q1.append(x)
         
         #add code here
     
    #Function to pop an element from queue and return that element.
    def pop(self):
        if len(self.q1)==0:
            return -1
        else:
            return self.q1.pop(0)
        
         