class Solution:
    def correctBST(self, root):
        # Helper function for in-order traversal to find misplaced nodes
        def find_misplaced_nodes(node):
            nonlocal prev, first, middle, last
            
            if node:
                # Traverse left subtree
                find_misplaced_nodes(node.left)
                
                # If previous node is greater than current node
                if prev and prev.data > node.data:
                    # If first misplaced node is not found yet
                    if not first:
                        first = prev
                        middle = node  # Potential second misplaced node
                    else:
                        last = node  # Update last misplaced node
                
                prev = node
                
                # Traverse right subtree
                find_misplaced_nodes(node.right)
        
        # Initialize variables to store misplaced nodes
        prev = None
        first = None
        middle = None
        last = None
        
        # Find misplaced nodes using in-order traversal
        find_misplaced_nodes(root)
        
        # If last misplaced node is not found, swap first and middle nodes
        if not last:
            first.data, middle.data = middle.data, first.data
        # Otherwise, swap first and last nodes
        else:
            first.data, last.data = last.data, first.data
        
        return root
