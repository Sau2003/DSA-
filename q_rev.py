from queue import Queue

class Solution:
    # Function to reverse the queue.
    def rev(self, q):
        stack = []

        # Dequeue all elements from the queue and push them onto the stack
        while not q.empty():
            stack.append(q.get())

        # Pop all elements from the stack and enqueue them back into the queue
        while stack:
            q.put(stack.pop())

        return q
