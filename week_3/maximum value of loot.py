n,capacity=map(int,raw_input().split())
total_weight=capacity
l=[]
values = []
weights = []
for i in range(0,n):
    value,weight=map(int,raw_input().split())
    values.append(value)
    weights.append(weight)
    ratio = value/(weight*1.0)
    l.append(ratio)
a = zip(l,values ,weights)
a.sort(reverse=True, key= lambda a : (a[0],-a[2]))
#print a
k=[]
prev=0
start=0
for i in a:
    if i[2]<=capacity :
        capacity=capacity - i[2]
        #print capacity
        k.append(i[2] * i[0])
    elif i[2]>capacity and int(prev)==prev:
        fraction=capacity*i[0]
        k.append((fraction))
        prev = capacity/(total_weight*1.0)
    else:
        k.append(0)
    if start==0:
        prev = k[0]
    start+=1        
#print k
total_profit=0
    
print("%.4f" % sum(k))
         
