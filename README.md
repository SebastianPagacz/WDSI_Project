# Table of contents
* [What is Simple ERP?](#What-is-simple-ERP?)
* [Technologies](#Technologies)
* [Development Environment Setup](#Development-Environment-Setup)
* [Product class](#Product-class)
* [Component-class](#Component-class)
* [Raport function](#raport-function)
* [Obliczenia function](#obliczenia-function)
  
# What is simple ERP?
Simple ERP is not complicated, basic and easy to use tool created to manage recourses of a company in a simple and user firendly manner.

# Technologies
Python3

# Development Environment Setup
Only thing requiered to use simple ERP is Python compiler. It is that simple!

# Product class
`Product` class takes 6 positional arguments, all which are required
```
Product(name, stock, demand, time_to_make, components_amount, final_time)
```
* First argument is `name`, it should be a string value, tells us the name of the product
* Second is `stock`, which should be a positive inteeger, tells us amount of product that we currently have
* Third is `demand`, also should be a positive inteeger, tells us demand for our product
* Fourth is `time_to_make`, also a positive inteeger, tells us about how much time it takes to make final product
* The fith one `components_amount`, for the code to work properly it has to be list of strings, tells us about amount of components that we need to make a single product
* The last one is `final_time`, this argument has to be positive inteeger, tells us in how many days there is a deadline 

# Component class
`Component` class takes 5 arguments, all of them are required, to create an object
```
Component(name, stock, order_time, time_to_make, amount_needed_in_product)
```
* First argument is `name`, it should be a string value, tells us the name of the component
* Second is `stock`, which should be a positive inteeger, tells us amount of component that we currently have
* Third is `order_time`, also should be a positive inteeger, tells us how many days it takes for components parts to be delivered
* Fourth is `time_to_make`, also a positive inteeger, tells us how much time it takes us to make component into the final product
* The last one from Component class is `amount_needed_in_product`, it also should be a positive inteeger number, tells us the amount of components that are required to make a final product

# raport function
`raport()` function returns a string containing full informations about our product and deadlines

# obliczenia function
`obliczenia()` function calculates and returns a string containing amounts and time within we have to place order in order to complete the order in time
