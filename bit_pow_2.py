class Solution:
    def isPowerofTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return n & (n - 1) == 0