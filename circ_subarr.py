def circularSubarraySum(arr, n):
    max_normal = arr[0]
    max_ending = arr[0]
    min_normal = arr[0]
    min_ending = arr[0]
    total_sum = arr[0]

    for i in range(1, n):
        total_sum += arr[i]
        # Update maximum subarray sum
        max_ending = max(arr[i], max_ending + arr[i])
        max_normal = max(max_normal, max_ending)
        # Update minimum subarray sum
        min_ending = min(arr[i], min_ending + arr[i])
        min_normal = min(min_normal, min_ending)

    # Calculate maximum circular subarray sum
    max_circular = total_sum - min_normal
    # If all elements are negative, return the maximum among them
    if max_circular == 0:
        return max_normal
    else:
        return max(max_circular, max_normal)
