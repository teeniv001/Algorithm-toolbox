##def gcd(a,b):
##    x=min(a,b)
##    for i in range(1,x+1):
##        if (a%i==0) and (b%i==0):
##            gcd=i
##    return (gcd)

# above function giving memory out of bound error


def gcd(x,y):
    while(y!=0):
        x,y=y,x%y
    return x

a,b=map(int,raw_input().split())
lcm = (a*b)/gcd(a,b)
print lcm
