#User function Template for python3
def eraseAt(deq, x):
    deq.rotate(-x)  # rotate the deque to bring the element at position x to the front
    deq.popleft()   # remove the element at the front (position x)
    deq.rotate(x)   # rotate the deque back to its original position
    return deq
#Function to erase the elements in range start (inclusive), end (exclusive).
def eraseInRange(deq, s, e):
    for i in range(e-1, s-1, -1):  # iterate in reverse from e-1 to s
        deq.rotate(-i)  # rotate the deque to bring the element at position i to the front
        deq.popleft()   # remove the element at the front (position i)
        deq.rotate(i)   # rotate the deque back to its original position
    return deq

#Function to erase all the elements in the deque.   
def eraseAll(deq):
    deq.clear()  # clear the deque
    return deq 
    #code here