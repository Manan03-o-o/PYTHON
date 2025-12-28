class Shop:
    def __init__(self):
        self.products = {"Laptop":50000, "Phone":20000}
        self.cart = {}

    def add_to_cart(self, item):
        if item in self.products:
            self.cart[item] = self.products[item]

    def bill(self):
        total = sum(self.cart.values())
        print("Items:", self.cart)
        print("Total Bill:", total)

shop = Shop()

while True:
    print("\n1.Add Item 2.Bill 3.Exit")
    ch = input("Choice: ")
    if ch == "1":
        shop.add_to_cart(input("Item: "))
    elif ch == "2":
        shop.bill()
    else:
        break
   