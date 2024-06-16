class Solution:
    ##Complete this function
    # Function to find the gray code of given number n
    def greyConverter(self, n):
        # Calculate the Gray code using the formula (n XOR (n >> 1))
        gray_code = n ^ (n >> 1)
        return gray_code


        ##Your code here

class Solution:    
    ##Complete this function
    # function to convert a given Gray equivalent n to Binary equivalent.
    def grayToBinary(self, n):
        binary = 0
        
        while n > 0:
            binary ^= n
            n >>= 1
        
        return binary
