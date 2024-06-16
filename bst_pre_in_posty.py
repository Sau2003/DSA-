def preOrder(root):
    result = []
    if root:
        result.append(root.val)
        result.extend(preOrder(root.left))
        result.extend(preOrder(root.right))
    return result


def InOrder(root):
    result = []
    if root:
        # Traverse the left subtree
        result.extend(InOrder(root.left))
        result.append(root.val)
        # Traverse the right subtree
        result.extend(InOrder(root.right))
    return result

def postOrder(root):
    result=[]
    if root:
        if root.left:
            result.extend(postOrder(root.left))
        if root.right:
            result.extend(postOrder(root.right))
        result.append(root.val)
    return result    