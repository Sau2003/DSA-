class Solution:
    
    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        # Helper function for in-order traversal to check if the tree is BST
        def is_bst_helper(node, min_val, max_val):
            # Base case: if the node is None, return True
            if not node:
                return True
            
            # Check if the current node's value is within the valid range
            if min_val < node.data < max_val:
                # Recursively check the left and right subtrees
                return (is_bst_helper(node.left, min_val, node.data) and
                        is_bst_helper(node.right, node.data, max_val))
            else:
                return False
        
        # Start the in-order traversal from the root
        return is_bst_helper(root, float('-inf'), float('inf'))
