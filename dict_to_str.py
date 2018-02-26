def dicttostr(d):
    s = "";
    for key, value in d.items():
        s += key+"="+value+";"
    s = s[:-1]
    return s;
       
d ={}                     
for i in range(2):        
    text = input().split()     
    d[text[0]] = text[1]           
print(dicttostr(d))
