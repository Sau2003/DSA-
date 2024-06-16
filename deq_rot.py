from collections import deque

# Function to rotate deque by k places in anti-clockwise direction.
def left_Rotate_Deq_ByK(deq, k):
    # Rotate deque by k places in anti-clockwise direction
    deq.rotate(-k)

# Function to rotate deque by k places in clockwise direction.   
def right_Rotate_Deq_ByK(deq, k):
    # Rotate deque by k places in clockwise direction
    deq.rotate(k)
