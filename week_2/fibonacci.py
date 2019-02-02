n=input() 
a = 0
b = 1
if n==0:
    print a
elif n==1:
    print 1
else:
    for i in range(2,n+1):
        c=a+b
        a=b
        b=c
    print b
