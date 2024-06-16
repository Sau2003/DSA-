def deleteFromArray(arr, n, idx):
    if idx >= 0 and idx < n:
        del arr[idx]  
        arr.append(0)  
    else:
        return -1  
    return arr 
