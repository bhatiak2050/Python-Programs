def great(list1=[]):
    g=list1[0]
    for i in list1:
        if i > g:
            g = i
    return g


list1=[]
n = int(input("Enter the limit: "));

for i in range(n):
    list1.append(int(input("Enter a number: ")))

print(great(list1))
