class Solution:
    # Function to return the count of non-repeated elements in the array.
    def printNonRepeated(self, arr, n):
        frequency = {}
        non_repeated = []
        for num in arr:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        # Traverse the original array to maintain the order
        for num in arr:
            if frequency[num] == 1:
                non_repeated.append(num)
        
        return non_repeated
