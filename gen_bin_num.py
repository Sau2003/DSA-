#Function to generate binary numbers from 1 to N using a queue.
def generate(N):
    res=[]
    for i in range(1,N+1):
        res.append(bin(i)[2:])
    return res    
        
    # code here
