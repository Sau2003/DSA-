class Solution:
    def longestConsecutiveOnes(self, N):
        # Initialize variables to store the maximum count of consecutive 1s and the current count
        max_count = 0
        count = 0

        # Iterate over the binary representation of N
        while N:
            # If the least significant bit is 1, increment the count
            if N & 1:
                count += 1
            else:
                # Update the max_count if the current count is greater
                max_count = max(max_count, count)
                # Reset the count
                count = 0
            # Right shift N to check the next bit
            N >>= 1

        # Update the max_count after the loop in case the longest consecutive sequence ends at the end of the binary representation
        max_count = max(max_count, count)

        return max_count