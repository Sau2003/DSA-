class Solution:
    def countBitsFlip(self, a, b):
        # XOR of A and B will give us a number with set bits at positions where bits differ between A and B.
        xor_result = a ^ b
        
        # Count the number of set bits in the XOR result.
        # We can use Brian Kernighan's Algorithm for this.
        count = 0
        while xor_result:
            xor_result &= (xor_result - 1)
            count += 1
        
        return count
