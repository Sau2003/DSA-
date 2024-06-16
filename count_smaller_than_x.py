class Solution:
    def smallerThanX(self,arr,n,x):
        arr.sort()
        count=0
        for i in arr:
            if i<x:
                count+=1
            else:
                break
        return count    

ob=Solution()
a=ob.smallerThanX([1,2,3,4,5],5,3) 
print(a)