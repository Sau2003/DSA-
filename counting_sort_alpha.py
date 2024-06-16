class Solution:
    # Function to arrange all letters of a string in lexicographical
    # order using Counting Sort.
    def countSort(self, arr):
        # Assuming ASCII characters, define the range
        K = 256  # Number of possible characters
        
        # Convert the string to a list of characters
        arr = list(arr)
        
        # Initialize output array and count array
        output = [0] * len(arr)
        count = [0] * K
        
        # Count occurrences of each character
        for x in arr:
            count[ord(x)] += 1
        
        # Cumulative sum of count array
        for i in range(1, K):
            count[i] += count[i - 1]
        
        # Place characters in output array in sorted order
        for x in reversed(arr):
            output[count[ord(x)] - 1] = x
            count[ord(x)] -= 1
        
        # Copy sorted characters back to the original array
        for i in range(len(arr)):
            arr[i] = output[i]
        
        # Join the sorted characters back into a string
        return "".join(arr)
