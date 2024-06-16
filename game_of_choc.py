import math
class Solution:
    # Function to decide who should play first
    def game(self,A, B):
        golden_ratio = (1 + math.sqrt(5)) / 2
        nimber = math.floor(abs(B - A) * golden_ratio)
        if nimber == min(A,B):
            return False
        else:
            return True 