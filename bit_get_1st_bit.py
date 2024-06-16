class Solution:
    def getFirstSetBit(self, n):
        # Get the binary representation as a string.
        binary_str = bin(n)[2:]  # [2:] to remove the '0b' prefix
        
        # Iterate over the string from right to left.
        for i in range(len(binary_str) - 1, -1, -1):
            if binary_str[i] == '1':
                # Position of the first set bit is (i + 1) from the right.
                return len(binary_str) - i
        return 0  # If no set bit is fou