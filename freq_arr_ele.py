def countg_feq(arr,n):
    h=dict()
    for i in range(n):
        if arr[i] in h.keys():
            h[arr[i]]+=1
        else:
            h[arr[i]]=1
    for x in h:
        print(x,'',h[x]) 

print(countg_feq([1,1,1,32,43],5))                   