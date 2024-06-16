class Solution:
    def countOnes(self, arr, N):
        l = 0
        h = N - 1
        if h >= l:
            mid = l + (h - l) // 2
            if (mid == h or arr[mid + 1] == 0) and arr[mid] == 1:
                return mid + 1
            if arr[mid] == 1:
                return self.countOnes(arr, mid + 1, h)
            else:
                return self.countOnes(arr, l, mid - 1)
        return 0



