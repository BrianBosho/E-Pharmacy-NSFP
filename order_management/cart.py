from .product import Product
from .stock import Stock

class Cart:
    """Represents a cart with a list of products and quantity

    Attributes:
        products: a dictionary with the key being the ID of the products, and the value being the quantity
        added
    """
    def __init__(self, stock: Stock) -> None:
        self.products = {}
        self.stock = stock

    def add(self, productCode: str, quantity: int):
        """Adds a product to the cart with the specified quantity
        
        Args:
            productCode: the identifier of the product
            quantity: quantity to add

        Returns: None
        """
        #TODO: Make sure the quantity is valid (> 0 and <= to the quantity in the stock)
        #TODO: If the product was already in the cart, increment the quantity        
        #TODO: After the checks, add the product to the dictionary
        product_list = self.stock.products  
        current_quantity = 0
        if productCode in self.products:
            current_quantity = self.products[productCode]

        for product in product_list:
            if product.code == productCode:
                if quantity > 0 and quantity <= product.quantity:
                    self.products[productCode] = quantity+ current_quantity
                    product.quantity -= quantity
                else:
                    print("Invalid quantity")

       

    def __str__(self) -> str:
        """String representation of the cart
        """
        #TODO: Return a string representation of a cart that shows the products, their quantity, unit price, total price. And also the total price of the cart
        # Feel free to format it the way you want to
        cart_products = self.products # returns a dictionary with product code and quantity
        # use product code to get a product object from the stock with its attributes
        product_string_list = []
        total_cart_price = 0
        for product_code in self.products:
            for item in self.stock.products:
                if product_code == item.code:
                    product_string = f"Product: {item.name}, Quantity: {cart_products[product_code]}, Unit Price: {item.price}, Total Price: {cart_products[product_code]*item.price}"
                    total_cart_price += cart_products[product_code]*item.price
                    product_string_list.append(product_string)

        return f"Cart: {product_string_list}, Total Cart Price: {total_cart_price}"
    
        
    def remove(self, code):
        """
        Removes a specific product from the cart """
        #TODO: Removes a product from the cart. safely fail if the product code is not found
        # add the quantity back to the stock
        q = self.products[code]
        for product in self.stock.products:
            if product.code == code:
                product.quantity += q
        del self.products[code]

    def clear(self):
        """Clears up the cart.
        """
        for cart_product in self.products:
            q= self.products[cart_product]
            for product in self.stock.products:
                if cart_product == product.code:
                    product.quantity += q
        self.products.clear()

    #clear cart for purchased items without increasing stock as was the case when removing and clearing items
    def clear_purchased(self):
        """Clears up the cart.
        """
        self.products.clear()

    @property
    def cost(self):
        """Returns the total cost of the cart"""
        #TODO: implement the function
        total_cart_price = 0
        for product_code in self.products:
            for item in self.stock.products:
                if product_code == item.code:                    
                    total_cart_price += self.products[product_code]*item.price
        return total_cart_price
    