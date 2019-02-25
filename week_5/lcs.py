def LCS(a,b,m,n):
    
    k = [[None]*(n+1) for i in xrange(m+1)] 
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0 : 
                k[i][j] = 0
            elif a[i-1] == b[j-1]: 
                k[i][j] = k[i-1][j-1]+1
            else: 
                k[i][j] = max(k[i-1][j] , k[i][j-1]) 
    return k[m][n] 

m=input()
a=raw_input().split()
s=[]
t=[]
for i in range(0,m):
    s.append(a[i])
n=input()
b=raw_input().split()
for i in range(0,n):
    t.append(b[i])


print LCS(a,b,m,n)
