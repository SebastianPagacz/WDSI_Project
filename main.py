class Product:
    def __init__(self, id, name, demand, stock, production_time, sec_lvl_components, sec_lvl_time, sec_lvl_stock, sec_lvl_amounts):
        self.id = id
        self.name = name
        self.demand = demand
        self.stock = stock
        self.demand_netto = self.stock - self.demand
        self.production_time = production_time
        self.sec_lvl_components = sec_lvl_components
        self.sec_lvl_time = sec_lvl_time
        self.sec_lvl_stock = sec_lvl_stock
        self.sec_lvl_amounts = sec_lvl_amounts


    #def __str__(self):
        #return f"Product id: {self.id} \nProduct name: {self.name} \nDemand: {self.demand} \nStock: {self.stock} \nProduction time: {self.production_time} \nNetto demand: {self.demand_netto} \nComponents: {self.sec_lvl_components}"
        
    def calculations(self):
        if self.demand_netto >= 0:
            return "We have the right amount of product in stock!"
        else:
            sec_lvl_netto = []
            for x in range(len(self.sec_lvl_stock)):
                res = self.sec_lvl_stock[x] - self.sec_lvl_amounts[x]*abs(self.demand_netto)
                sec_lvl_netto.append(res)
                for y in sec_lvl_netto:
                    if y >=0:
                        


product = Product(1, "tort", 1, 0, 2, ["polewa", "ciasto", "wisienka"], [1, 2, 1], [5, 10, 2], [2, 1, 1])
#print(product)
print(product.calculations())