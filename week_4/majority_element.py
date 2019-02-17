n=input()
m=map(int,raw_input().split())
high=0
count=1
m.sort()
z=int(n/2)
k=[]
l=[]

for i in range(0,n):
    k.append(m[i])

for i in range(0,n-1):
    if k[i]==k[i+1]:
        count+=1
        
    elif k[i]!=k[i+1]:
        l.append(count)
        count=1
    if i==n-2:
        l.append(count)

for i in range(0,len(l)):
    if l[i]>high:    
        high=l[i]   
    else:
        pass

if high>z:
    print 1
else:
    print 0
        


