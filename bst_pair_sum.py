
def findPair(root, X):
    # Stack for iterative in-order traversal
    stack_left, stack_right = [], []
    curr_left, curr_right = root, root
        
        # Initialize pointers for leftmost and rightmost nodes
    while curr_left:
        stack_left.append(curr_left)
        curr_left = curr_left.left
    while curr_right:
        stack_right.append(curr_right)
        curr_right = curr_right.right
        
    # Iterate until pointers meet or cross each other
    while stack_left and stack_right and stack_left[-1] != stack_right[-1]:
        left_val, right_val = stack_left[-1].key, stack_right[-1].key
        
        # If the sum is equal to X, return True
        if left_val + right_val == X:
            return True
            
            # If the sum is less than X, move the left pointer to the next larger value
        elif left_val + right_val < X:
            # Move left pointer to the next larger value
            curr_left = stack_left.pop().right
            while curr_left:
                stack_left.append(curr_left)
                curr_left = curr_left.left
            
            # If the sum is greater than X, move the right pointer to the next smaller value
        else:
                # Move right pointer to the next smaller value
            curr_right = stack_right.pop().left
            while curr_right:
                stack_right.append(curr_right)
                curr_right = curr_right.right
        
        # If no pair is found, return False
    return False