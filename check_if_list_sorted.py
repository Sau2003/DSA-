# Efficient 

def sorted(l):
    i=1
    while i<len(l):
        if l[i]<l[i-1]:
            return False
        i+=1
        
        return True
        
# Another method is directly using the sorted function 