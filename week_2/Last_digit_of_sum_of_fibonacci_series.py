#this code partially solves the problem, fibo series of length upto 12 digits
#if anyone's solution is accepted then do merge the solution at my github


n=input()
a=0
b=1
c=a+b
sum_=0
if n==0:
    print (a)
    sum_=0
elif n==1:
    print (b)
    sum_=1
elif n==2:
    sum_=2
    print (sum_)
else:
    sum_=2
    for i in range(0,n-2):
        a=b%10
        b=c%10
        c=(a+b)
        sum_=(sum_+c)
    print (sum_%10)
    
