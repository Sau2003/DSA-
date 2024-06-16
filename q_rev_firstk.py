from collections import deque

class Solution:
    def modifyQueue(self, q, k):
        # Convert queue to deque for efficient manipulation
        q = deque(q)
        
        # Create a deque to temporarily store the first K elements
        temp = deque()
        for _ in range(k):
            temp.appendleft(q.popleft())  # Use appendleft() to add elements to the left
        
        # Re-enqueue the reversed elements back into the queue
        for _ in range(k):
            q.append(temp.popleft())
        
        # Re-enqueue the remaining elements back into the queue
        for _ in range(len(q) - k):
            q.append(q.popleft())
        
        return q