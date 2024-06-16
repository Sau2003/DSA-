class Solution:
    def insertAtIndex(self, arr, sizeOfArray, index, element):
        if index >= 0 and index <= sizeOfArray - 1:  # Check if index is within bounds
            arr.append(0)  # Add a placeholder element at the end
            for i in range(sizeOfArray, index, -1):
                arr[i] = arr[i - 1]  # Shift elements to the right
            arr[index] = element  # Insert the element at the specified index
        else:
            return -1  # Return -1 if insertion is not possible
        return arr 