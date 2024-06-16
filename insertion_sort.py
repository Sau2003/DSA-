def merge_list(a,b):
    res=[]
    m=len(a)
    n=len(b)
    i=0
    j=0
    while i<m and j<n:
        if a[i]<b[j]:
            res.append(a[i])
            i+=1
        else:
            res.append(b[i])
            j+=1
    while i<m:
        res.append(a[i])
        i+=1
    while j<m:
        res.append(b[j])
        j+=1
    return res                    