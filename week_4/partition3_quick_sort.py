#partition3
import random
def partition(arr, l, r):

    low = l  
    i = l   
    high = r
    pivot = arr[l]    
    while i <= high:      
        if arr[i] < pivot:
            arr[low], arr[i] = arr[i], arr[low]
            low += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[high] = arr[high], arr[i]
            high -= 1
        else:
            i += 1
            
    return low, high



def quicksort(arr, l, r):
    if l >= r: 
        return
    low, high = partition(arr, l, r)
    quicksort(arr, l, low - 1)
    quicksort(arr, high + 1, r)

n=input()
k=map(int,raw_input().split())
arr=[]
for i in range(0,n):
    arr.append(k[i])
quicksort(arr,0,n-1)

print " ".join(map(str,arr))
