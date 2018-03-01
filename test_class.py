class menu1:
    def __init__(self, n):
        self.list1=[]
        for i in range(n):
            self.list1.append(str(input("Enter item: ")))
    def getmenu(self):
        return self.list1

n = int(input("How many elements to begin with??"))
ob = menu1(n)
print(ob.getmenu())
