from main1 import Component, Product

ciasto = Component("Ciasto", 3, 3, 2, 1)
polewa = Component("Polewa", 5, 1, 1, 2)
wisienka = Component("Wisienka", 2, 2, 0, 1)

tort = Product("Tort", 1, 50, 1, [ciasto, wisienka, polewa], 1)

Returns report about stock and gives us information about product and components
print(tort.raport())
Calculates amounts and time within we have to place order for components
print(tort.obliczenia())
