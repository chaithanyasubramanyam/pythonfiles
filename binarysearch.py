def search(x,l):
    n = len(l)//2 + 1
    if l[n-1] == x:
        print('found')
    elif l[n-1] > x and len(l) > 1:
        return search(x,l[:n-1])
    elif l[n-1] < x and len(l) > 1:
        return search(x,l[n:])
    else:
        print('not found')

l = list(map(int,input().split()))
l.sort()
x = int(input())
search(x,l)


    

