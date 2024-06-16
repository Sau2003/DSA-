#User function Template for python3
from collections import deque

#dq : deque in which element is to be pushed
#x : element to be pushed


#Function to push element x to the front of the deque.
def push_front_pf(dq,x):
    dq.appendleft(x)
    return dq
    #code here
    

#Function to push element x to the back of the deque.
def push_back_pb(dq,x):
    dq.append(x)
    return dq
    #code here
    
#Function to return element from front of the deque.
def front_dq(dq):
    if dq:
        return dq[0]
    else:
        return -1  
    
#Function to pop element from back of the deque.
def pop_back_ppb(dq):
    if dq:
        return dq.pop()
    else:
        return -1