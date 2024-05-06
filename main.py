class Product:
    def __init__(self, id, name, demand, stock, production_time):
        self.id = id
        self.name = name
        self.demand = demand
        self.stock = stock
        self.demand_netto = self.demand - self.stock
        self.production_time = production_time

    def __str__(self):
        return f"Product id: {self.id} \nProduct name: {self.name} \nDemand: {self.demand} \nStock: {self.stock} \nProduction time: {self.production_time} \nNetto demand: {self.demand_netto}"
        

product = Product(1, "tort", 1, 0, 2)
print(product)
