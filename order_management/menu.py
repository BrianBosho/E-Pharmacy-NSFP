from . import Stock, Cart, User, UserManagement, BookRecords, Wrapper, Prescription

MSG_WRONG_INPUT = "Wrong input. Try again!"
class Menu:
    """Represents the menu class for the project

    Attributes: 
        stock: stock variable
        profiles: user management module
        pharmacist: account of the salesperson
        records_file: path to the file containing the sales
        prescriptions_file: path to the file containing the prescriptions.
        stock_file: path to the file containing the stock data
    """
    def __init__(self, stock: Stock, profiles: UserManagement, pharmacist: User, records_file: str, prescriptions_file: str, stock_file: str) -> None:
        self.stock = stock
        self.profiles = profiles
        self.pharmacist = pharmacist
        self.cart = Cart(stock = stock)
        # use the file instead of the object so that we can keep track
        self.records_file = records_file
        self.prescriptions_file = prescriptions_file
        self.stock_file = stock_file

    #TODO: Create all the necessary functions/method to create and manage the menu using the
    # available variables and all the attributes of the class

    def main_menu(self):
        print("1. Order management")
        print("2. Analytics")
        print("0. Exit")
        main_choice = input("Enter your choice: ")
        if main_choice == "1":
            self.order_menu()
        elif main_choice == "2":
            self.analytics_menu()
        elif main_choice == "0":
            exit()
        else:
            print(MSG_WRONG_INPUT)
            self.main_menu()


    def order_menu(self):
        order_menu = True
        while(order_menu):
            print("1. Adding to a cart")
            print("2. Remove from a cart")
            print("3. Clear the cart")
            print("4. Checkout")
            print("0. Back")
            order_choice = input("Enter your choice: ")
            if order_choice == "1":
                add_to_cart = True
                while(add_to_cart):
                    print("select product")
                    list_counter = 1
                    for product in self.stock.products:
                        print(f"{list_counter}.  {product.name} | {product.price}  | {product.quantity}")
                        list_counter += 1           
                
                    product_choice = input("select product by number: ")            
                    product_quantity = input("Enter number: ")
                    selected_product = self.stock.products[int(product_choice)-1].code
                    self.cart.add(selected_product, int(product_quantity))
                    choice = input("Add another product? (y/n): ")
                    if choice == "y":
                        add_to_cart = True
                    elif choice == "n":
                        add_to_cart = False
                    else:
                        print(MSG_WRONG_INPUT)
                        add_to_cart = False

                
                
            elif order_choice == "2":
                print("Remove from cart")
                # show items in cart
                cart_products = self.cart.products
                print("select product to remove")
                list_counter = 1
                list_items = []
                for product in cart_products:
                    for item in self.stock.products:
                        if product== item.code:
                            print(f"{list_counter}.  {item.name} | {item.price}  | {cart_products[product]}")
                            list_items.append(item.code)
                            list_counter += 1
                selected_item =input("select product by number: ")
                item_code = list_items[int(selected_item)-1]
                self.cart.remove(item_code)
                # ask user to select item to remove   
            elif order_choice == "3":   
                choice =input("Clear cart? (y/n): ")
                if choice == "y":
                    self.cart.clear()
                elif choice == "n":
                    self.order_menu()
                else:
                    print(MSG_WRONG_INPUT)
                    self.order_menu()
            elif order_choice == "4":
                #show teh items in cart
                
                for product_code in self.cart.products:
                    for product in self.stock.products:
                        if product_code == product.code:
                            print(f"{product.name} | {product.price}  | {self.cart.products[product_code]}")
                print(f"Total: {self.cart.cost}")
                choice=input("confirm purchase? (y/n): ")
                if choice == "y":
                    print("purchase confirmed")
                    self.cart.clear_purchased()
                elif choice == "n":
                    print("purchase cancelled")
                else:
                    print(MSG_WRONG_INPUT)
                    self.order_menu()               

            elif order_choice == "0":
                self.main_menu()
            else:
                print(MSG_WRONG_INPUT)
                self.order_menu()
        

    def analytics_menu(self): 
        sales_file = 'data/sales.json'
        books = BookRecords.load(sales_file)      
        print("1. Total income from purchases")
        print("2. Prescription statistics")
        print("3. Purchases for a user")
        print("4. Sales by an agent")
        print("5. Top sales")
        print("0. Back")
        analytics_choice = input("Enter your choice: ") 
        if analytics_choice == "1":
            print("Total income from purchases")
            # we can get this from BookRecords.totaltransactions()
            #create an instance of book records
            
            print(f"The total transactions is: {books.totalTransactions()}")

        elif analytics_choice == "2":
            print(f"Prescription statistics: \n {books.reportOnPrescriptions()}")
        elif analytics_choice == "3":
            name = input("Enter user name: ")
            purchases =books.purchasesByUser(name)
            print(purchases)
            
            # print("Purchases for a user")
        elif analytics_choice == "4":
            name = input("Enter salesperson name: ")
            sales =books.salesByAgent(name)
            print(sales)
        elif analytics_choice == "5":
            print("Top 10 sales \n")
            top_sales = books.topNSales()
            print(top_sales)
        elif analytics_choice == "0":
            self.main_menu()

    # Make sure to dump the prescriptions, stock, and sale data after every sale.

    # Your menu should have two main options with sub-options. Such as
    """
    1. Order management
        1.1. Adding to a cart (you need to show the list of products and ask the user to select one with ID. Bonus: Can you display with numbers and ask user to choose a number instead?
                Also ask for quantity.)
        1.2. Remove from a cart (display the cart and ask the user to select the element to remove. Remove by ID or by index (bonus))
        1.3. Clear the cart (self explanatory)
        1.4. Checkout (displays the cart with the total and ask for a prescription element. Proceed to checkout and show a message is successful or not).
    2. Analytics
        2.1. Total income from purchases
        2.2. Prescription statistics
        2.3. Purchases for a user
        2.4. Sales by an agent
        2.5. Top sales

    * For each of the menu items, when necessary, display a success or error message to guide the user.
    """

    # **CHALLENGE** (BONUS): Can you implement the menu to work as a USSD application? Implement and show your design