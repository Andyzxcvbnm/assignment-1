def rever(a):
    b = a.reverse()
    c = [' ','!','@','#','$','%','^','&','*','(',')'
        ,'?']
    a = a.discard(c)
    b = b.discard(c)
    if a in b:
        print True
    else:
        print False
    
