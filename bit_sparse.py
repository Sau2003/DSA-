#User function Template for python3

class Solution:
    def isSparse(self, n):
        # Convert the number to its binary representation
        binary = bin(n)[2:]
        
        # Iterate through the binary representation
        for i in range(1, len(binary)):
            # Check if consecutive set bits are found
            if binary[i] == '1' and binary[i-1] == '1':
                return 0
        
        # If no consecutive set bits are found, return 1
        return 1
