class menu():
    def __init__(self):
        self = []
        n = int(input("How many elements to begin with??"))
        for i in range(n):
            self.append(input("Enter name: "));
    def getmenu(self):
        return self

ob = menu()
print(ob.getmenu())
