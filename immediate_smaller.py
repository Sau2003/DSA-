class Solution:
    def immediateSmaller(self,arr,n,x):
        arr.sort()
        s=[]
        for i in arr:
            if i<x:
                s.append(i)
            else:
                break
        if not s:
            return -1
        return max(s)        
