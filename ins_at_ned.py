def insertAtEnd(arr, sizeOfArray, element):
    if len(arr) < sizeOfArray:
        arr.append(element)
    else:
        return -1
    return arr

print(insertAtEnd([1,2,3,4], 6, 9))
