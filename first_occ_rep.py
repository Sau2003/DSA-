class Solution:
    def firstRepeated(self, arr, n):
        # Create a dictionary to store the last seen index of each element
        last_seen = {}
        
        # Initialize the result to -1
        result = -1
        
        # Iterate through the array
        for i in range(n):
            # If the current element is already in the dictionary,
            # update the result if it's -1 or if the current index is smaller
            if arr[i] in last_seen:
                if result == -1 or last_seen[arr[i]] < result:
                    result = last_seen[arr[i]]
            else:
                # Otherwise, store the current index as the last seen index
                last_seen[arr[i]] = i + 1  # Adjust for 1-based indexing
        
        # Return the result
        return result