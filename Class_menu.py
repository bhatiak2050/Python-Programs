class menu1:
    def __init__(self, n):
        self.dict1={}
        for i in range(n):
            self.dict1.update({str(input("Enter item name: ")):int(input("Enter item price: "))})

    def getmenu(self):
        return self.dict1

    def getitem(self, item):
        return self.dict1[item]

    def additem(self, item):
            self.dict1.append(item)
            print(item+" successfully added to menu\n")

    def deleteitem(self, item):
            for i in self.dict1:
                if i == item:
                    self.dict1.remove(item)
                    print(item+" successfully removed from menu\n")
                    return ;
            print("Item not found\n")

n = int(input("How many elements to begin with??"))
ob = menu1(n)

while(1):
    print("Menu:\n1)Add item to menu\n2)Remove element from menu\n3)Get price of an item\n4)Show menu\n5)Exit")
    choice = int(input("\nEnter your choice: "))

    if choice==1:
        ob.additem(str(input("Enter item name: ")),str(input("Enter item Price: ")),)
    elif choice==2:
        ob.deleteitem(str(input("Enter item name: ")))

    elif choice==3:
        ob.getitem(str(input("Enter item name: ")))

    elif choice==4:
        print("\nThe menu contains:")
        print(ob.getmenu())
        print("")
    else:
        break
