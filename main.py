""" Principios de Diseño de Software
    Programa que implementa abstracción en un sistema de empresas de comida
"""

from abc import ABC, abstractmethod

class Company(ABC):
    @abstractmethod
    def getSales(self):
        pass
    
    @abstractmethod
    def getProducts(self):
        pass

class Products(ABC):
    @abstractmethod
    def createProduct(self):
        pass
    
    def deliverProduct(self):
        pass
    
    
class Pizza(Products):
    def createProduct(self):
        print("Cooking pizza")
        
    def deliverProduct(self):
        print("Delivering pizza")
    
class Bread(Products):
    def createProduct(self):
        print("Cooking bread")
        
    def deliverProduct(self):
        print("Delivering bread")
        
        
class Pizzeria(Company):
    def getProducts(self):
        return [Bread(), Pizza()]
    
    def getSales(self):
        return print("providing sales for pizzeria")

class Bakery(Company):
    def getProducts(self):
        return [Bread()]
    
    def getSales(self):
        return print("providing sales for bakery")

def main():
    pizzeria1 = Pizzeria()
    
    for product in pizzeria1.getProducts():
        print(product.createProduct())
        print(product.deliverProduct())
        
if __name__ == "__main__":
    main()