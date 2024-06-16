class Solution:
    def posOfRightMostDiffBit(self, m, n):
        # If both numbers are the same, return -1.
        if m == n:
            return -1
        
        # Find the rightmost different bit using XOR.
        xor_result = m ^ n
        
        # Find the position of the rightmost set bit in xor_result.
        # We can do this by finding the position of the least significant set bit (LSB).
        # The position of the LSB is 1-indexed from the right.
        # Example: LSB of 0101 is at position 1, LSB of 1000 is at position 4.
        return (xor_result & -xor_result).bit_length()