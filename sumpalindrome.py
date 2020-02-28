
line = int(input())
c = 0
palindrom = False
while palindrom == False:
    c += 1
    w = list(str(line))
    w.reverse()
    line2 = ''.join(w)
    s = int(line) + int(line2)
    l = list(str(s))


    i = 0
    j = len(l) - 1
    while i < len(l)//2:

            
        if l[i] == l[j]:
            i += 1
            j -= 1
            k = 0
        else:
            k = 1
            break
    if k == 0:
        palindrom = True
    else:
        palindrom = False
        line = s
        
                
        
   
print(c,s)
