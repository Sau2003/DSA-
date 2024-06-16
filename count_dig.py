def Count(n):
    res=0
    while n>0:
        n=n//10
        res+=1
    return res

n=int(input("Enter the number "))
a=Count(n)
print(a)
    
