class Solution:
    def getCount(self, root, low, high):
        # Helper function for in-order traversal to count nodes within range
        def count_nodes_in_range(node, low, high):
            # Base case: if node is None, return 0
            if not node:
                return 0
            
            # Initialize count as 0
            count = 0
            
            # If node value is within the range, increment count
            if low <= node.data <= high:
                count += 1
            
            # If node value is greater than low, traverse left subtree
            if node.data > low:
                count += count_nodes_in_range(node.left, low, high)
            
            # If node value is less than high, traverse right subtree
            if node.data < high:
                count += count_nodes_in_range(node.right, low, high)
            
            return count
        
        # Start in-order traversal from root
        return count_nodes_in_range(root, low, high)