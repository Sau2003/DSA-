class Solution:
    def isSorted(self, arr, n):
        # Check if the array is increasingly sorted
        for i in range(1, n):
            if arr[i] < arr[i - 1]:
                break
        else:
            return 1  # Array is increasingly sorted

        # Check if the array is decreasingly sorted
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                break
        else:
            return 1  # Array is decreasingly sorted

        return 0
        #code here
