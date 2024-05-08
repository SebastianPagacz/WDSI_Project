class Product:
    def __init__(self, prod_name):
        self.prod_name = prod_name
        self.prod_stock = 0
        self.prod_demand = 0
        self.prod_time_to_make = 0
        self.prod_components_amount = 0

    def set_prod_stock(self, amount):
        self.prod_stock = int(amount)

    def set_prod_demand(self, amount):
        self.prod_demand = int(amount)

    def __str__(self):
        if self.prod_stock - self.prod_demand > 0:
            return f"Product name: {self.prod_name} \nProduct stock: {self.prod_stock} \nProduct demand: {self.prod_demand} \nWe have enough stock to complete. \nStock after completing the order: {self.prod_stock - self.prod_demand}."
        else:
            return f"Product name: {self.prod_name} \nProduct stock: {self.prod_stock} \nProduct demand: {self.prod_demand} \nWe dont have enough stock. \nStock that we need to complete: {abs(self.prod_stock - self.prod_demand)}."
        

product = Product("Tort")
product.set_prod_stock(10)
product.set_prod_demand(5)
print(product)