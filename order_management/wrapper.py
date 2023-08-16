from .cart import Cart
from .stock import Stock
from .product import Product
from .prescription import Prescription
from datetime import datetime
import random

import json

## would need to create a new object for each new order
class Wrapper:
    """
    Main class used to manage orders and carts.

    Attributes:
        sales: A list of the sales done during the program's execution
        stock: The stock used in the execution
        agentID: the username of the pharmacist running the program
    """
    def __init__(self, stock: Stock, agentID: str) -> None:
        self.sales = []
        self.stock = stock
        self.agentID = agentID

    def checkout(self, cart: Cart, customerID: str, prescription: Prescription = None):
        """Handles the checkout procedure of the program.
        
        Args:
            cart: The cart to pay for
            prescription: the prescription that accompanies the order (default: None)
        """

        #TODO: First check that all the product that require a prescription have all the criteria met
        # (i.e., (1) there is a prescription that (2) matches the customer's ID, and (3) contains the medication
        # in the specified quantity).
        # Raise an exception if either of those conditions is unmet.

        # check the products in the cart and identify those that need prescriptions
        # cart_sales = []
        product_list = self.stock.products
        try:
            for item in cart.products:
                for product in product_list:
                    if item == product.code:
                        cart_product = product
                        if (cart_product.requires_prescription == True):
                            if prescription != None:
                                if customerID == prescription.CustomerID: 
                                # check if quantity of product in cart matches quantity of medication in prescription
                                #quantity from medications list
                                    for medication in prescription.Medications:
                                        if cart_product.name == medication["name"]:
                                            if cart.products[item] == medication["quantity"]:
                                                pass
                                            else:
                                                raise Exception("Quantities do not match")
                                                
                                            
                                else:
                                    raise Exception("Customer ID does not match")
                                    
                                
                            else:
                                raise Exception("Prescription required")
                                return
                            
                            
                        else:
                            pass
            
                        date_time = datetime.now()
                        id = random.randint(1000, 9999)
                        sale = {
                            "id": str(id),
                            "name": cart_product.name,
                            "quantity": cart.products[item],
                            "price": cart_product.price,
                            "purchase_price": cart_product.price * cart.products[item],
                            "timestamp": date_time.timestamp(),
                            "customerID": customerID,
                            "salesperson": self.agentID,
                            "prescriptionID": prescription.PrescriptionID if prescription != None else None                         
                        }
                        self.sales.append(sale)
                        if prescription != None:
                            prescription.markComplete(cart_product)
        except Exception as e:
            print(f"Error: {e}")
    
                    
                            
                


        #TODO: Get the current datetime and save a Sale information for each product sold with the following schema
        # {"name": "<name>", "quantity": <quantity>, "price": <unit price>, "purchase_price": <total price>, "timestamp": <timestamp>,
        # "customerID": <customer username>, "salesperson": <pharmacist username>}

        #TODO: Append the list to the current sales

  
        # sales_file = 'data/sales.json'
        # with open (sales_file, "r") as file:
        #     sales_list = json.load(file)

        

        #TODO: Make sure that the sold products are marked as complete in the prescriptions.

    def dump(self, outfile: str):
        """Dumps the current sales data to a file

        Args:
            outfile: the path to the output file
        """
        #TODO: Load the content, if any of the existing file
        with open (outfile, "r") as file:
            sales_list = json.load(file)
        
        #TODO: Update the content by appending the new entries to it, and save to the file
        sales_list.extend(self.sales)
        with open (outfile, "w") as file:
            json.dump(sales_list, file)