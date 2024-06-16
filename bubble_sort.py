def bubble_sort(l):
    for i  in range(len(l)-1):
        swapped=False
        for j in range(n-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
                swapped=True
            if swapped==False:
                return 
                
