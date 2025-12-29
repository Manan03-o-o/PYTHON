class Ecommerce:
    def __init__(self):
        self.products = {"Laptop":50000, "Phone":20000, "Headphones":3000}
        self.cart = {}

    def show_products(self):
        for p, price in self.products.items():
            print(p, "₹", price)

    def add_to_cart(self, item):
        if item in self.products:
            self.cart[item] = self.products[item]

    def checkout(self):
        total = sum(self.cart.values())
        print("Items:", self.cart)
        print("Total Bill:", total)

shop = Ecommerce()

while True:
    print("\n1.Show 2.Add 3.Checkout 4.Exit")
    ch = input("Choice: ")
    if ch == "1":
        shop.show_products()
    elif ch == "2":
        shop.add_to_cart(input("Item: "))
    elif ch == "3":
        shop.checkout()
    else:
        break
    