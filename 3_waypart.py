#User function template for Python
class Solution:
    def threeWayPartition(self, array, a, b):
        # Initialize three pointers: low, mid, and high
        low = 0
        mid = 0
        high = len(array) - 1
        
        # Iterate through the array
        while mid <= high:
            # If the current element is less than a, swap it with the element at low index
            if array[mid] < a:
                array[mid], array[low] = array[low], array[mid]
                low += 1
                mid += 1
            # If the current element is between a and b, move to the next element
            elif a <= array[mid] <= b:
                mid += 1
            # If the current element is greater than b, swap it with the element at high index
            else:
                array[mid], array[high] = array[high], array[mid]
                high -= 1
        
        # Return the modified array
        return array