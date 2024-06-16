class Solution:
    
    # Function to find maximum of each subarray of size k.
    def max_of_subarrays(self, arr, n, k):
        dq = deque()  # Corrected the initialization
        max_values = []  # List to store maximum elements of subarrays
        for i in range(k):
            while dq and arr[i] >= arr[dq[-1]]:
                dq.pop()
            dq.append(i)
        max_values.append(arr[dq[0]])
        for i in range(k, n):
            while dq and dq[0] <= i - k:
                dq.popleft()
            while dq and arr[i] >= arr[dq[-1]]:
                dq.pop()
            dq.append(i)
            max_values.append(arr[dq[0]])
        return max_values
        #code here
