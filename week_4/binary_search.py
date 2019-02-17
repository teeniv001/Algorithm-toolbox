def search(n, k, item):
    low = 0
    high = k - 1

    index=-1
    while low <= high:
        mid = (low + high)/2
        if n[mid]==item:
            index = mid
            break
        elif n[mid] > item:
            high = mid - 1
        elif n[mid] < item:
            low = mid + 1
    return index

n = map(int, raw_input().split())
k = n[0]
del n[0]

searches = map(int, raw_input().split())
del searches[0]

for item in searches:
    print search(n, k, item), 

