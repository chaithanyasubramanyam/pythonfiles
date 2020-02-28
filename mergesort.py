def merge(arr,l,r):
    i = j = k = 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1
    if i == len(l) and j < len(r):
        while j < len(r):
            arr[k] = r[j]
            j += 1
            k +=1
    if j == len(r) and i < len(l):
        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1






def mergesort(arr):
    if len(arr) >1:
        m = len(arr)//2
        l = arr[:m]
        r = arr[m:]
        mergesort(l)
        mergesort(r)
        merge(arr,l,r)

arr = [100, 22, 5, 2, 6, 1]
mergesort(arr)
for i in arr:
    print(i,end=' ')
