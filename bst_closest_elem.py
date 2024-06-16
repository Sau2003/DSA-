#User function Template for python3

class Solution:
    
    # Function to find the least absolute difference between any node
    # value of the BST and the given integer.
    def minDiff(self, root, K):
        # Initialize minimum absolute difference
        min_diff = float('inf')
        
        # Stack to perform iterative in-order traversal
        stack = []
        curr = root
        
        # Iterate until the stack is empty or current node is not None
        while stack or curr:
            # Traverse left subtree and push nodes onto stack
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Pop the top node from stack
            curr = stack.pop()
            
            # Update minimum absolute difference
            min_diff = min(min_diff, abs(curr.data - K))
            
            # Traverse right subtree
            curr = curr.right
        
        return min_diff