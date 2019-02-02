a,b=map(int,raw_input().split())
x=min(a,b)
for i in range(1,x+1):
    if (a%i==0) and (b%i==0):
        gcd=i
print i

############  2nd approach  ##########

 
##import math                            # since math function also uses eular gcd so it is fast
##print math.gcd(a,b)

############   3rd approach #########

##def recursive_solution(x,y):
##    while(y!=0):
##        x,y = y,x%y                   #example( 40,10) in first time x=10 and y=4
##    return x                          #                in second time x=4 and y=2
##                                      #                in third time x=2 and y=0 so it return 2
##
##print recursive_solution(a,b)




#but time complexity in all three approach



