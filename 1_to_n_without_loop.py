class Solution:    
    def printNos(self, N):
        if N == 0:
            return 
        else:
            self.printNos(N - 1)
            print(N)

# Instantiate the Solution class
sol = Solution()

# Call the printNos method
sol.printNos(5)
