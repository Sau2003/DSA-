class BIT:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)
        
    def update(self, idx, value):
        while idx <= self.size:
            self.tree[idx] += value
            idx += idx & -idx
    
    def query(self, idx):
        sum = 0
        while idx > 0:
            sum += self.tree[idx]
            idx -= idx & -idx
        return sum

def countSmallerRight(arr, n):
    if not arr:
        return 0

    # Coordinate compression
    sorted_unique = sorted(set(arr))
    rank = {val: idx + 1 for idx, val in enumerate(sorted_unique)}

    # Initialize BIT
    bit = BIT(len(rank))

    # To store the count of distinct smaller elements for each element
    count_smaller = [0] * n
    
    # Traverse the array from right to left
    seen = set()
    for i in range(n - 1, -1, -1):
        current_rank = rank[arr[i]]
        
        # Query the number of elements that are smaller than the current element
        count_smaller[i] = bit.query(current_rank - 1)
        
        # Update the BIT only if the element is seen for the first time
        if arr[i] not in seen:
            bit.update(current_rank, 1)
            seen.add(arr[i])
    
    # Return the maximum count found
    return max(count_smaller)