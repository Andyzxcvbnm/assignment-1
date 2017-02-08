def maps(s,n):
    n=int(n)
    result=[ ]
    for i in s:
        result.append(len(i))
    while result<n:
        result+=1
    else:
        print result+1
