def LCS3(a,b,u,m,n,p):
    
    k = [[[0 for i in range(p+1)] for j in range(n+1)] for k in range(m+1)]  
    for i in range(m+1): 
        for j in range(n+1):
            for v in range(p+1):
                if i == 0 or j == 0 or v==0: 
                    k[i][j][v] = 0
                elif a[i-1] == b[j-1] and a[i-1]==c[v-1]: 
                    k[i][j][v] = k[i-1][j-1][v-1]+1
                else: 
                    k[i][j][v] = max(k[i-1][j][v] , k[i][j-1][v], k[i][j][v-1]) 
    return k[m][n][p] 

s=[]
t=[]
u=[]
m=input()
a=raw_input().split()
for i in range(0,m):
    s.append(a[i])
n=input()
b=raw_input().split()
for i in range(0,n):
    t.append(b[i])
p=input()
c=raw_input().split()
for i in range(0,p):
    u.append(c[i])

print LCS3(a,b,u,m,n,p)
