from collections import deque

class Solution:
    
    # Function to return a list of nodes visible from the top view 
    # from left to right in Binary Tree.
    def topView(self, root):
        if not root:
            return []
        
        # Dictionary to store nodes at each horizontal distance
        top_view_nodes = {}
        
        # Queue for level-order traversal along with horizontal distance
        queue = deque([(root, 0)])
        
        # Perform level-order traversal
        while queue:
            node, hd = queue.popleft()
            
            # If this horizontal distance is not yet encountered, add the node
            if hd not in top_view_nodes:
                top_view_nodes[hd] = node.data
            
            # Enqueue left child with horizontal distance one less than current node
            if node.left:
                queue.append((node.left, hd - 1))
            
            # Enqueue right child with horizontal distance one more than current node
            if node.right:
                queue.append((node.right, hd + 1))
        
        # Sort the top view nodes based on horizontal distance
        sorted_top_view = sorted(top_view_nodes.items(), key=lambda x: x[0])
        
        # Extract the node values and return
        result = [val for hd, val in sorted_top_view]
        return result
