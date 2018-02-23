def getcs(server,dbname, usr, mypass):
    #server=mysrvr;dbname=mydb;usr=me;pass=mypass
    s = "server="+server+";dbname="+dbname+";usr="+usr+";pass="+mypass
    return s


server = input("Enter server name: ")
dbname = input("Enter database name: ")
usr = input("Enter user name: ")
mypass = input("Enter pass name :");

print(getcs(server,dbname,usr,mypass))
