def great(a,b,c):
    #g = (a>b)?((a>c):a:c):((b>c)?b:c))
    if(a>b):
        if(a>c):
            return a
        else:
            return c
    elif(b>c):
        return b
    else:
        return c
        

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
g = great(a, b, c)
print(g)



            
