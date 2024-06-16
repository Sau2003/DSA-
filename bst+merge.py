class Solution:
    
    # Function to return a list of integers denoting the node 
    # values of both the BST in a sorted order.
    def merge(self, root1, root2):
        # Helper function for in-order traversal
        def in_order_traversal(node, result):
            if node:
                in_order_traversal(node.left, result)
                result.append(node.data)
                in_order_traversal(node.right, result)
        
        # Perform in-order traversal on both trees
        merged_result = []
        in_order_traversal(root1, merged_result)
        in_order_traversal(root2, merged_result)
        
        # Sort the merged result
        merged_result.sort()
        
        return merged_result
