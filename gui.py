from tkinter import *


class Restaurant(Frame):

    def __init__(self, master):
        super(Restaurant, self).__init__(master)
        self.grid()
        self.show_content()
        self.temp = []
        self.fileWriter = ''

    def show_content(self):
        # create instruction label
        Label(self, text="Welcome to The IIT Restaurant", font="Helvetica 16 bold italic",
              fg="dark green").grid(column=1, columnspan=3, sticky=W)
        # Name
        Label(self, text="Name:").grid(row=2, column=0, sticky=W)
        self.varName = StringVar()
        Entry(self, textvariable=self.varName).grid(row=2, column=1, sticky=W)
        # Address
        Label(self, text="Address:").grid(row=2, column=3, sticky=W)
        self.varAddress = StringVar()
        Entry(self, textvariable=self.varAddress).grid(row=2, column=4, sticky=W)

        Label(self, text="What Would you Like to Order!", font="Helvetica 10 bold italic", fg="blue", anchor="e").grid(
            columnspan=2)

        # pizza
        self.varPizza = BooleanVar()
        Checkbutton(self, text="Pizza(Tk 500)", anchor="e", variable=self.varPizza).grid(row=4, column=0, sticky=W)
        self.varPizzaCount = StringVar()
        Spinbox(self, from_=0, to=10, textvariable=self.varPizzaCount).grid(row=4, column=1, sticky=W)

        # Burger
        self.varBurger = BooleanVar()
        Checkbutton(self, text="Burger(Tk 200)", anchor="e", variable=self.varBurger).grid(row=5, column=0, sticky=W)
        self.varBurgerCount = StringVar()
        Spinbox(self, from_=0, to=10, textvariable=self.varBurgerCount).grid(row=5, column=1, sticky=W)

        # Sandwich
        self.varSandwich = BooleanVar()
        Checkbutton(self, text="Sandwich(Tk 100)", anchor="e", variable=self.varSandwich).grid(row=6, column=0,
                                                                                               sticky=W)
        self.varSandwichCount = StringVar()
        Spinbox(self, from_=0, to=10, textvariable=self.varSandwichCount).grid(row=6, column=1, sticky=W)

        # Drinks
        self.varDrinks = BooleanVar()
        Checkbutton(self, text="Drinks(Tk 50)", anchor="e", variable=self.varDrinks).grid(row=7, column=0, sticky=W)
        self.varDrinksCount = StringVar()
        Spinbox(self, from_=0, to=10, textvariable=self.varDrinksCount).grid(row=7, column=1, sticky=W)

        # Receipt
        Label(self, text="Order Summery: ").grid(row=3, column=3, sticky=W)
        self.varReciept = Text(self, width=35, height=15, wrap=WORD)
        self.varReciept.grid(row=4, column=3, rowspan=6, columnspan=3, sticky=W)

        # Order Type
        Label(self, text="Select Order Type!", font="Helvetica 10 bold italic", anchor="e", fg="blue").grid(row=8,
                                                                                                            columnspan=2)
        self.varType = StringVar()
        self.varType.set("Dining")
        Radiobutton(self, text="Dining", variable=self.varType, value="Dining").grid(row=9, column=0, sticky=W)
        Radiobutton(self, text="Home Delivery", variable=self.varType, value="Home Delivery").grid(row=9, column=1)

        # Button
        Button(self, text="Order", bg="green", fg="White", command=self.getData).grid(row=12, column=0, sticky=NSEW)
        Button(self, text="Reset", bg="red", fg="White", command=self.reset).grid(row=12, column=1, sticky=NSEW)
        Button(self, text="Confirm Payment ", bg="blue", fg="White", command=self.payment).grid(row=12, column=3,
                                                                                                columnspan=2,
                                                                                                sticky=NSEW)

        # Discount
        Label(self, text="Discount:", anchor="e").grid(row=10, column=0, sticky=W)
        self.varDiscount = StringVar()
        Entry(self, textvariable=self.varDiscount).grid(row=10, column=1, sticky=W)
        self.varDiscount.set(0)


        # Sub-Total
        Label(self, text="Total Payment:", anchor="e").grid(row=11, column=3, sticky=W)
        self.varPayment = StringVar()
        Entry(self, textvariable=self.varPayment).grid(row=11, column=4, sticky=W)

    def getData(self):
        self.total = 0
        self.dicount = 0
        name = 'Customer Name: ' + self.varName.get() + '\n'
        address = 'Customer Address: ' + self.varAddress.get() + '\n' + "--------------------------------\n\n"
        orderItem = "Item-------Count--------Total" + '\n'

        if self.varPizza.get():
            pizza = 500 * int(self.varPizzaCount.get())
            orderItem += "Pizza" + "--------" + self.varPizzaCount.get() + "-----------" + str(pizza) + '\n'
            self.total = self.total + pizza
        if self.varBurger.get():
            burger = 200 * int(self.varBurgerCount.get())
            orderItem += "Burger" + "-------" + self.varBurgerCount.get() + "-----------" + str(burger) + '\n'
            self.total = self.total + burger
        if self.varSandwich.get():
            sandwich = 100 * int(self.varSandwichCount.get())
            orderItem += "Sandwich" + "-----" + self.varSandwichCount.get() + "-----------" + str(sandwich) + '\n'
            self.total = self.total + sandwich
        if self.varDrinks.get():
            drinks = 50 * int(self.varDrinksCount.get())
            orderItem += "Drinks" + "-------" + self.varSandwichCount.get() + "-----------" + str(drinks) + '\n'
            self.total = self.total + drinks
        if self.varType.get() == "Dining":
            delivery = 0
            orderItem += "Delivery Fee:" + "------------" + str(delivery) + '\n'
            self.total = self.total + delivery
        elif self.varType.get() == "Home Delivery":
            delivery = 50
            orderItem += "Delivery Fee:" + "------------" + str(delivery) + '\n'
            self.total = self.total + delivery
        discountItem = "Discount:" + "----------------" + self.varDiscount.get() + '\n'
        self.total -= int(self.varDiscount.get())
        totalItem = "\n\n-----------------------------\nTotal-------------------" + str(self.total)+'\n'
        self.fileWriter = name + address + orderItem + discountItem + totalItem
        print(name, address)
        self.varReciept.delete(0.0, END)
        self.varReciept.insert(0.0, self.fileWriter)

    def payment(self):
        wd = Tk()
        wd.title("Confirmation")
        wd.config(height=300, width=300)
        if self.varPayment.get() >= str(self.total):
            self.fileWriter+="Paid-------------------"+self.varPayment.get()+'\n'
            self.fileWriter += "Return-------------------" + str(int(self.varPayment.get())-self.total) + '\n'
            self.varReciept.delete(0.0, END)
            self.varReciept.insert(0.0, self.fileWriter)
            lblSuccess = Label(wd, text="Success\n Thank You for Ordering from\n The XYZ Restaurant\n", fg="green")
            lblSuccess.place(relx=0.5, rely=0.5, anchor=CENTER)
            btnPrint = Button(wd, text="Print Receipt", fg="Black", command=self.receiptPrint)
            btnPrint.place(relx=0.5, rely=0.6, anchor=CENTER)
        else:
            lblFiled = Label(wd, text="Failed!\n Please Enter a Valid Amount", fg="red")
            lblFiled.place(relx=0.5, rely=0.5, anchor=CENTER)

    def reset(self):
        self.varName.set('')
        self.varAddress.set('')
        self.varPizza.set(0)
        self.varPizzaCount.set(0)
        self.varBurger.set(0)
        self.varBurgerCount.set(0)
        self.varSandwich.set(0)
        self.varSandwichCount.set(0)
        self.varDrinks.set(0)
        self.varDrinksCount.set(0)
        self.varReciept.delete("1.0", "end")
        self.varPayment.set('')
        self.varDiscount.set(0)

    def receiptPrint(self):
        with open('receipt.txt', 'w') as the_file:
            the_file.write(self.fileWriter)


root = Tk()
root.title("IIT Restaurant")
root.geometry("600x400")
app = Restaurant(root)
root.mainloop()
