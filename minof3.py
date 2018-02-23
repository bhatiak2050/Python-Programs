def minof3(a,b,c):
    return a if a<b else b if b<c else c

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print(minof3(a,b,c))
