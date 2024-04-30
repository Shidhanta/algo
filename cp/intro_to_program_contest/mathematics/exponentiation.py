# exponentiation function 
# recursion 
def exp(a,n):
    if n==0: return 1
    if n==1 : return a
    t = exp(a,n//2)
    return t*t*(exp(a,n%2))

# iterative 
def exp2(a,n):
    pwr = 1
    while(n>0):
        if(n==1):
            pwr=pwr*a
            break
        else:
            pwr*=a
            n-=1
    return pwr
