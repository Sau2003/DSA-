class Solution:
    def swapBits(self, N):
        # Mask to extract all even bits
        mask_even = 0xAAAAAAA  # 1010...10 (in binary)

        # Mask to extract all odd bits
        mask_odd = 0x55555555   # 0101...01 (in binary)

        # Extract even bits and shift them to the right by 1 position
        even_bits = (N & mask_even) >> 1

        # Extract odd bits and shift them to the left by 1 position
        odd_bits = (N & mask_odd) << 1

        # Combine shifted even and odd bits using bitwise OR operation
        result = even_bits | odd_bits

        return result