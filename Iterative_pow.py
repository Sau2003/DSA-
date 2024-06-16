# Iterative Power (Binary Exponentiation)

def power(x,n) :
    
    res = 1 
    
    while n > 0 :
        if n % 2 != 0 :
            res = res * x 
        x = x * x
        n = n // 2 
    
    return res 
    

x = 4
n = 5
print(power(x,n))