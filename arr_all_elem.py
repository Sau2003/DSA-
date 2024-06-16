class Solution:
    def printArrayRecursively(self, arr, n):
        if n == 0:
            return
        self.printArrayRecursively(arr, n - 1)  # Recursively print elements before the nth element
        print(arr[n - 1], end=" ")
ob=Solution()  
arr=[12,1,3,14,2]
print(ob.printArrayRecursively(arr,5))         
