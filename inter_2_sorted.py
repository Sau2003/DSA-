class Solution:
    #Function to return a list containing the intersection of two arrays.
    def printIntersection(self, a, b, n, m):
        set1 = set(a)
     
        # Removing duplicates from the first array
        result = []
     
        # Avoiding duplicates and adding intersections
        for num in b:
            if num in set1:
                result.append(num)
                set1.remove(num)
     
        return result