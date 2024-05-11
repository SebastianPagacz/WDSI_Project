class Component:
    def __init__(self, comp_name, comp_stock, comp_order_time, comp_time_to_make, comp_to_make):
        self.comp_name = comp_name
        self.comp_stock = comp_stock
        self.comp_order_time = comp_order_time
        self.comp_time_to_make = comp_time_to_make
        self.comp_to_make = comp_to_make

class Product:
    def __init__(self, prod_name, prod_stock, prod_demand, prod_time_to_make, prod_components_amount, prod_final_time):
        self.prod_name = prod_name
        self.prod_stock = prod_stock
        self.prod_demand = prod_demand
        self.prod_time_to_make = prod_time_to_make
        self.prod_components_amount = prod_components_amount
        self.prod_final_time = prod_final_time

    def raport(self):
        raport_res =  f"Product name: {self.prod_name} \nProduct stock: {self.prod_stock} \nProduct demand: {self.prod_demand} \n"
        if self.prod_stock - self.prod_demand > 0:
            raport_res += f"We have enough stock to complete. \nStock after completing the order: {self.prod_stock - self.prod_demand}. \nComponents: \n"
            for x in range(len(self.prod_components_amount)):
                raport_res +=f"{self.prod_components_amount[x].comp_name} \n"
            return raport_res[0:-1]
        else:
            raport_res += f"We dont have enough stock. \nStock that we need to complete: {abs(self.prod_stock - self.prod_demand)}. \nComponents: \n"
            for x in range(len(self.prod_components_amount)):
                raport_res +=f"{self.prod_components_amount[x].comp_name} \n"
            return raport_res[0:-1]
        
    def obliczenia(self):
        demand_component = []
        if self.prod_demand > self.prod_stock:
            for x in range(len(self.prod_components_amount)):
                if self.prod_components_amount[x].comp_stock - (self.prod_components_amount[x].comp_to_make * self.prod_demand) < 0:
                    demand_component.append(abs(self.prod_components_amount[x].comp_stock - (self.prod_components_amount[x].comp_to_make * self.prod_demand)))
                else:
                    demand_component.append(0)
        if sum(demand_component) == 0:
            return "we have everything in stock"
        else:    
            res_obliczenia = "We need: \n"
            for x in range(len(self.prod_components_amount)):
                res_obliczenia += f"{self.prod_components_amount[x].comp_name}: {abs(self.prod_components_amount[x].comp_stock - (self.prod_components_amount[x].comp_to_make * self.prod_demand))} pieces \n"
                comp1_order = self.prod_final_time - (self.prod_components_amount[0].comp_order_time + self.prod_components_amount[0].comp_time_to_make + 1)
            res_obliczenia += "\nOrder: \n"
            for x in range(len(self.prod_components_amount)):
                res_obliczenia += f"{self.prod_components_amount[x].comp_name} in: {comp1_order} days\n" 
            return res_obliczenia
                
ciasto = Component("Ciasto", 30, 3, 2, 1)
polewa = Component("Polewa", 50, 1, 1, 2)
wisienka = Component("Wisienka", 25, 2, 0, 1)


tort = Product("Tort", 1, 5, 1, [ciasto, wisienka, polewa], 10)

print(tort.raport())
#print(tort.obliczenia())