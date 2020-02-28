def partition(arr,low,high):
    p = arr[low]
    i = low+1
    j = high
    while i <= j:
        if arr[i] > p:
            if arr[j] < p:
                arr[i],arr[j] = arr[j],arr[i]
                i += 1
                j -= 1
            else:
                j -= 1
        else:
            i += 1
    arr[low],arr[j] = arr[j],arr[low]
    return j

def quicksort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)

arr = list(map(int,input().split()))
n = len(arr)
quicksort(arr,0,n-1)
for i in arr:
    print(i,end=' ')
