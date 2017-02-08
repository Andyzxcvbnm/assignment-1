def translate(c):
    a = {'merry':'god','christmas':'jul','and':'och','happy':'gott','new':'nytt','year':'ar'}
    b = a.keys()
    if c in b:
        print a[c]
    else:
        print'wrong'
