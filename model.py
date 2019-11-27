class Menu:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Payment:
    def __init__(self, price):
        self.price = price

    def pay(self, amount):
        print("total amount is " + str(self.price))
        print("paid amount is " + str(amount))


class User:
    def __init__(self, name):
        self.name = name


class Customer(User):

    def __init__(self, name):
        super().__init__(name)


class Manager(User, Menu):
    menu = Menu

    def __init__(self, name):
        super().__init__(name)


menuList = []


def start():
    user = int(input("select user:\n1.Manager\n2.Customer\n3.exit\ntype here:"))
    uName = input("Your name: ")

    if user == 2:
        cUser = Customer(uName)
        count = 0
        for menu in menuList:
            count += 1
            print(count, menu.name, menu.price)

        orderedItems = []

        count = int(input("How many Item you like to order?"))

        for i in range(count):
            j=int(input("Menu Number:"))
            orderedItems.append(Menu(menuList[j-1].name,menuList[j-1].price))
        print("Items you have ordered:")
        count = 0
        total = 0
        for menu in orderedItems:
            count += 1
            print(count, menu.name, menu.price)
            total += menu.price
        print("Total Bill is:", total)
        payment=Payment(total)
        payment.pay(int(input("paid Amount:")))
        print("Thank You",cUser.name,"for using this software")
        start()
    elif user == 1:
        cUser = Manager(uName)
        menuList.append(Menu("Pizza", 100))
        menuList.append(Menu("Burger", 200))
        menuList.append(Menu("Fried Chicken", 150))
        menuList.append(Menu("Chicken Roll", 180))
        menuList.append(Menu("Sandwich", 250))
        menuList.append(Menu("Noodles", 210))
        menuList.append(Menu("Soup", 120))
        menuList.append(Menu("Drinks", 80))
        more = input(" 8 default Menu created. want to create more?(yes/no)")
        if more == 'yes':
            count = int(input("Enter Count of Menu:"))
            for i in range(count):
                menuList.append(Menu(input("Name: "),int(input("price: "))))
                print("Menu Added")
            print("Thank You",cUser.name,"for using this software")
        else:
            print("Thank You",cUser.name,"for using this software")

        start()
    else:
        print("Thanks You",uName)


start()
