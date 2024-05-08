class Component:
    def __init__(self, comp_name, comp_stock, comp_demand, comp_order_time, comp_time_to_make, comp_to_make):
        self.comp_name = comp_name
        self.comp_stock = comp_stock
        self.comp_demand = comp_demand
        self.comp_order_time = comp_order_time
        self.comp_time_to_make = comp_time_to_make
        self.comp_to_make = comp_to_make

class Product:
    def __init__(self, prod_name, prod_stock, prod_demand, prod_time_to_make, prod_components_amount):
        self.prod_name = prod_name
        self.prod_stock = prod_stock
        self.prod_demand = prod_demand
        self.prod_time_to_make = prod_time_to_make
        self.prod_components_amount = prod_components_amount

    def raport(self):
        if self.prod_stock - self.prod_demand > 0:
            return f"Product name: {self.prod_name} \nProduct stock: {self.prod_stock} \nProduct demand: {self.prod_demand} \nWe have enough stock to complete. \nStock after completing the order: {self.prod_stock - self.prod_demand}. \nComponents: \n{self.prod_components_amount[0].comp_name} \n{self.prod_components_amount[1].comp_name} \n{self.prod_components_amount[2].comp_name}"
        else:
            print(f"Product name: {self.prod_name} \nProduct stock: {self.prod_stock} \nProduct demand: {self.prod_demand} \nWe dont have enough stock. \nStock that we need to complete: {abs(self.prod_stock - self.prod_demand)}. \nComponents: {self.prod_components_amount[0]}")
            
    def obliczenia(self):
        demand_component = []
        if self.prod_demand > self.prod_stock:
            for x in range(len(self.prod_components_amount)):
                if self.prod_components_amount[x].comp_stock - self.prod_components_amount[x].comp_demand < 0:
                    demand_component.append(abs(self.prod_components_amount[x].comp_stock - self.prod_components_amount[x].comp_demand))
                else:
                    demand_component.append(0)
        return demand_component

ciasto = Component("Ciasto", 30, 20, 3, 2, 1)
polewa = Component("Polewa", 50, 20, 1, 1, 2)
wisienka = Component("Wisienka", 25, 20, 2, 0, 1)


tort = Product("Tort", 1, 5, 1, [ciasto, wisienka, polewa])

print(tort.obliczenia())
#print(tort.raport())