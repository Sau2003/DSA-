class Solution:
    def findFloor(self, A, N, X):
        l = 0
        h = N - 1
        floor_index = -1 

        while l <= h:
            mid = (l + h) // 2

            if A[mid] == X:
                return mid 

            elif A[mid] < X:
                floor_index = mid  
                l = mid + 1  

            else:
                h = mid - 1 

        return floor_index 