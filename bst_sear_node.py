def minValue(self, root):
    if root is None:
        return None
    if root.left is None:
        return root.data  # If left child is None, current node is the minimum
    return self.minValue(root.left) 