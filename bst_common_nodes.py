class Solution:
    
    # Function to find the nodes that are common in both BST.
    def findCommon(self, root1, root2):
        common_nodes = []  # List to store common nodes
        
        stack1, stack2 = [], []
        curr1, curr2 = root1, root2
        
        while stack1 or stack2 or curr1 or curr2:
            # Traverse left subtree of both BSTs
            while curr1:
                stack1.append(curr1)
                curr1 = curr1.left
            while curr2:
                stack2.append(curr2)
                curr2 = curr2.left
            
            # Pop top nodes from both stacks
            if stack1:
                curr1 = stack1.pop()
            if stack2:
                curr2 = stack2.pop()
            
            # If both nodes are not None, compare their values
            if curr1 and curr2:
                if curr1.data == curr2.data:
                    common_nodes.append(curr1.data)
                    # Move to the right subtree of both nodes
                    curr1 = curr1.right
                    curr2 = curr2.right
                elif curr1.data < curr2.data:
                    # Move to the right subtree of the first node
                    curr1 = curr1.right
                    # Reset the second node to its original position
                    stack2.append(curr2)
                    curr2 = None
                else:
                    # Move to the right subtree of the second node
                    curr2 = curr2.right
                    # Reset the first node to its original position
                    stack1.append(curr1)
                    curr1 = None
            # If one of the nodes is None, break the loop
            else:
                break
        
        return common_nodes