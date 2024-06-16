#User function Template for python3

class Solution:
    '''
    Function Arguments :
    		@param  : q (given list on which queue is implemented)
    		@param  : x (value to be used accordingly)
    		@return : None
    '''
    
    # Function to push an element in queue.
    def enqueue(self, q, x):
        q.append(x)

    # Function to remove front element from queue.
    def dequeue(self, q):
        if len(q) > 0:
            return q.pop(0)
        else:
            return None  # Returning None if queue is empty

    # Function to find the front element of queue.
    def front(self, q):
        if len(q) > 0:
            return q[0]
        else:
            return None  # Returning None if queue is empty

    # Function to find an element in the queue.
    def find(self, q, x):
        return x in q
