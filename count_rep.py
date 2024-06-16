class Solution:
    def findRepeating(self, arr, N):
        if len(arr) == 0:
            return (-1, -1)

        # Check if the array is sorted and consecutive
        is_consecutive = True
        for i in range(1, len(arr)):
            if arr[i] != arr[i - 1] + 1:
                is_consecutive = False
                break

        # If the array is sorted and consecutive
        if is_consecutive:
            return (-1, -1)

        # Binary search to find the repeating element
        s = 0
        e = len(arr) - 1
        while s < e:
            m = (s + e) // 2

            # If arr[m] == m + arr[0], there is no repeating character in [s..m]
            if arr[m] == m + arr[0]:
                s = m + 1
            # If arr[m] < m + arr[0], there is a repeating character in [s..m]
            else:
                e = m

        # The repeating element is arr[s]
        repeating_element = arr[s]
        # Calculate the frequency of the repeating element
        frequency = N - (arr[-1] - arr[0])

        return (repeating_element, frequency)
