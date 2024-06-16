def floor(root, x):
    res = None
    while root != None:
        if root.data == x:
            return root.data
        elif root.data > x:
            root = root.left
        else:
            res = root
            root = root.right
    return res.data if res else -1
            