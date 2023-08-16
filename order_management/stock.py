import json
from typing import List
from .product import Product

class Stock:
    """Represents the catalog of products
    
    Attributes:
        products: the list of products
    """
    def __init__(self, products: List[Product]) -> None:
        self.products = products

    def update(self, id: int, change: int):
        """Update the quantity of a product by adding or removing
        
        Args:
            id: identifier of the product
            change: the value by which the quantity should be update (+1 adds 1, -2 removes 2 for example)
        """
        #TODO: Make sure the product exists, and that by making the change, the value is still >= 0
        
        #TODO: Update the quantity
        product = self.getProductByID(id)
        if product is not None:
            if product is not None and product.quantity + change >= 0:
                product.quantity += change

    def getProductByID(self, id: int) -> Product:
        """Gets a product by its ID

        Args:
            id: identifier of the product
        
        Returns: the product's object
        """
        #TODO: Implement te function
        for product in self.products:
            if product.id == id:
                return product
        return None
        
    def dump(self, outfile: str):
        """Saves the stock to a JSON file"""
        #TODO: Implement the function
        product_list = [product.__dict__ for product in self.products]
        
        # Create a dictionary to store the list of products
        stock_data = {"products": product_list}
        
        # Save the data to the specified JSON file
        with open(outfile, 'w') as f:
            json.dump(stock_data, f, indent=4)
    
    @staticmethod
    def load(infile: str)-> 'Stock':
        """Loads the stock from an existing file
        
        Args: 
            infile: input file to the function
            
        """
        #TODO: Implement the function
            # self, 
            # code: int, 
            # name: str, 
            # brand: str,
            # description: str,
            # quantity: int, 
            # price: float, 
            # dosage_instruction: str,
            # requires_prescription: bool,
            # category: str) -> None:
        with open(infile, 'r') as file:
            prod_list = json.load(file)  
                 
        products = [Product(element['code'], element['name'], element['brand'], element["description"], element["quantity"], element["price"], element["dosage_instruction"], element["requires_prescription"], element["category"] ) for element in prod_list]
        
        return Stock(products)
        
    
    def __str__(self) -> str:
        """Returns a string representation of the stock
        """
        #TODO: Return the description of the stock with a nice output showing the ID, Name, Brand, Description, Quantity, Price, and the requires_prescription field
        