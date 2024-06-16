#Function to push an element in queue by using 2 stacks.
def Push(x, stack1, stack2):
    '''
    x: value to push
    stack1: list
    stack2: list
    '''
    # Push all elements from stack1 to stack2
    while stack1:
        stack2.append(stack1.pop())
    
    # Push the new element onto stack1
    stack1.append(x)
    
    # Push all elements back from stack2 to stack1
    while stack2:
        stack1.append(stack2.pop())

#Function to pop an element from queue by using 2 stacks.
def Pop(stack1, stack2):
    '''
    stack1: list
    stack2: list
    '''
    # If stack1 is empty, the queue is empty
    if not stack1:
        return -1
    
    # Pop the top element from stack1
    return stack1.pop()
