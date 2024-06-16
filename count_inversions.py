def count_iv(arr,l,r):
    res=0
    if (l<r):
        m=(l+r)//2
        res+=count_iv(arr,l,m)
        res+=count_iv(arr,m+1,r)
        res+=count_merge(arr,l,m,r)
    return res

def count_merge(arr,l,m,r):
    left=arr[l:m+1]
    right=arr[m+1:r+1]
    res,i,j,k=0,0,0,l
    while i<len(left)  and j<len(right):
        if left[i]<=right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[i]
            j+=1
            res+=(len(left)-i)
        K+=1
    while i<len(left):
        arr[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        arr[k]=right[j]
        j+=1
        k+=1