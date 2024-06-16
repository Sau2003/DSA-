class Solution:
    def closer(self, arr, N, x):
        # Initialize left and right pointers
        left = 0
        right = N - 1
        
        # Perform binary search
        while left <= right:
            mid = left + (right - left) // 2
            
            # If x is found at mid
            if arr[mid] == x:
                return mid
            
            # Check if the adjacent elements are closer to x
            if mid - 1 >= left and arr[mid - 1] == x:
                return mid - 1
            if mid + 1 <= right and arr[mid + 1] == x:
                return mid + 1
            
            # If x is less than the middle element, search in the left half
            if arr[mid] > x:
                right = mid - 2
            # If x is greater than the middle element, search in the right half
            else:
                left = mid + 2
        
        # If x is not found
        return -1
