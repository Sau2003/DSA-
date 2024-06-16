def GCD(a, b):
    while b:
        a, b = b, a % b
    return a

a, b = map(int, input("Enter the values of a and b separated by a comma: ").split(","))
c = GCD(a, b)
print(f"The GCD of {a} and {b} is {c}")



def GCD(a,b):
    while a!=b:
        if a>b:
            a=a-b
        
        else:                          # Euclidean Algo 
            b=b-a
        
    return a

a=GCD(4,6)
print(a)




def GCD(a,b):
    if b==0:
        return a
    else:
        return GCD(b,a%b)         # Modified Euclidean 

a=GCD(4,6)
print(a)