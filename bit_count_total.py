class Solution:
    def countSetBits(self, n):
        res = 0
        for i in range(1, n+1):
            num = i
            while num:
                num = num & (num - 1)
                res += 1
        return res