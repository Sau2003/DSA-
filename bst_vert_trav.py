from collections import defaultdict, deque

class Solution:
    
    # Function to find the vertical order traversal of Binary Tree.
    def verticalOrder(self, root): 
        if not root:
            return []
        
        # Dictionary to store nodes at each horizontal distance
        vertical_order = defaultdict(list)
        
        # Queue for level-order traversal
        queue = deque([(root, 0)])
        
        # Perform level-order traversal
        while queue:
            node, hd = queue.popleft()
            
            # Add the node to the vertical order dictionary at its horizontal distance
            vertical_order[hd].append(node.data)
            
            # Enqueue left child with horizontal distance one less than current node
            if node.left:
                queue.append((node.left, hd - 1))
            
            # Enqueue right child with horizontal distance one more than current node
            if node.right:
                queue.append((node.right, hd + 1))
        
        # Sort the vertical order dictionary based on horizontal distance
        sorted_vertical_order = sorted(vertical_order.items(), key=lambda x: x[0])
        
        # Concatenate the lists of nodes at each horizontal distance into a single list
        result = [node for hd, nodes in sorted_vertical_order for node in nodes]
        return result
