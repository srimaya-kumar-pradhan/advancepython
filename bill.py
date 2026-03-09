class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class BillingSystem:
    def __init__(self):
        self.cart = []
        self.transactions = []

    def add_product(self, name, price):
        product = Product(name, price)
        self.cart.append(product)
        print(name, "added to cart")

    def generate_bill(self, discount):
        total = 0

        print("\n------ BILL ------")
        for product in self.cart:
            print(product.name, ":", product.price)
            total += product.price

        print("Total:", total)

        discount_amount = total * discount / 100
        final_amount = total - discount_amount

        print("Discount:", discount, "%")
        print("Amount to Pay:", final_amount)

        self.transactions.append(final_amount)
        self.cart.clear()

    def show_transactions(self):
        print("\nTransactions:")
        for t in self.transactions:
            print("Bill Amount:", t)



billing = BillingSystem()

billing.add_product("Milk", 40)
billing.add_product("Bread", 30)
billing.add_product("Eggs", 60)

billing.generate_bill(10)   

billing.show_transactions()