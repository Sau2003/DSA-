def fun(n):
    if n<0:
        return "factorial not def"
    elif n==0:       
        return 1
    else:
        return n*fun(n-1)
    
n=int(input("Enter "))
a=fun(n)
print(a)    

    
