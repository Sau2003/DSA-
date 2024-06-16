class Solution:
    def findCeil(self, root, inp):
        res = None
        while root != None:
            if root.key == inp:
                return root.key
            elif root.key < inp:
                root = root.right
            else:
                res = root
                root = root.left
        return res.key if res else -1
