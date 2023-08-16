from __future__ import annotations

import json
from datetime import datetime

from typing import List
from .sale import Sale

class BookRecords:
    """A record of all the sales made through the application.
    
    Attributes:
        transactions: a list of the transactions
    """
    def __init__(self, transactions: List[Sale]) -> None:
        self.transactions = transactions
    
    def __str__(self) -> str:
        """Returns a string representation of a record. 
        
        Args:
        
        Returns: A string
        """

        #TODO: In the format below, return a representation of the records
        # |      # | Date                | Customer   | Medication | Quantity | Purchase Price | Prescription |
        # |      1 | 2023-06-03 21:23:25 | doe        | Quinine    |        3 |       1400 RWF | PHA1         |

        position = 0
        records_str = ""
        for transaction in self.transactions:
            position = position + 1
            transaction_str = f"{position} | {transaction.timestamp} | {transaction.customerID} | {transaction.quantity} | {transaction.purchase_price} | {transaction.prescriptionID}"
            records_str = records_str + transaction_str + "\n"
        return records_str
    def reportOnPrescriptions(self) -> str:
        """Reports on prescription sales.

        Args: 

        Returns: A string report of the prescriptions processed
        """
        #TODO: From the transactions data, retrieve for each prescription, the actual medications that were processed
        # and aggregate for each, the corresponding total price.
       
       #check if the sale has a prescription ID, if it has one, use the prescription ID to get the prescription object, then find the name of the medication in the prescription object
        prescription_str = ""
        position =0
        for sale in self.transactions:
            if sale.prescriptionID != None:
                position = position+1
                sale_str = f"| {position} | {sale.prescriptionID} | {sale.purchase_price} |"
                prescription_str = prescription_str + sale_str + "\n"
        return prescription_str



        #TODO: output in the following format, the results: 
        # |    # | Prescription ID | Total Price |

    def purchasesByUser(self, customerID: str):
        """Reports on the sales performed by a customer.
        
        Args:
            customerID: Username of the customer.

        Returns: A string representation of the corresponding transactions
            
        """
        #TODO: Query the transactions to the `transactions` list below
        # customer_transactions = ""
        # for transaction in self.transactions:
        #     if transaction.customerID == customerID:
        #         transaction_str = f"{transaction} \n"
        #         customer_transactions = customer_transactions + transaction_str
        transactions = []
        for customer_transactions in self.transactions:
            if customer_transactions.customerID == customerID:
                transactions.append(customer_transactions)
        if len(transactions)==0:
            return "No purchases by that user!"

                
        # transactions = None

        return BookRecords(transactions).__str__()

    def salesByAgent(self, salesperson: str):
        """Reports on the sales performed by a pharmacist.
        
        Args:
            salesperson: Username of the pharmacist.

        Returns: A string representation of the corresponding transactions
            
        """
        #TODO: Query the transactions to the `transactions` list below
        transactions = None
        transactions = []
        for customer_transactions in self.transactions:
            if customer_transactions.salesperson == salesperson:
                transactions.append(customer_transactions)
        if len(transactions)==0:
            return "No purchases by that user!"

        # return the string representation
        return BookRecords(transactions).__str__()
    
    def topNSales(self, start: datetime = datetime.strptime('1970-01-02', '%Y-%m-%d'), end: datetime = datetime.now(), n = 10) -> str:
        """Return the top n sales ordered by the total price of purchases.

        Args:
            start: a datetime representing the start period to consider (datetime, default to 01 Jan 1970)
            end: a datetime representing the end period to consider (datetime, default to current timestamp)
            n: number of records to consider (int, default to 10)

        Returns:
        A string representation of the top n 
        """
        #TODO: Query the top transactions and save them to the variable `transactions` below
        transactions = []
        #identify the transactions and sort them by teh price.
        for transaction in self.transactions:
            transactions.append(transaction)
        transactions.sort(key=lambda x: x.purchase_price, reverse=True)

        # return the string representation of the transactions.
        return BookRecords(transactions).__str__()


    def totalTransactions(self) -> float:
        """Returns the total cost of the transactions considered.
        
        Args:
        
        Returns: A floating number representing the total price
        """
        return sum([transaction.purchase_price for transaction in self.transactions])
    
    @classmethod
    def load(cls, infile: str) -> BookRecords:
        """Loads a JSON file containing a number of sales object
        
        Args:
            infile: path to the file to be read
        Returns: A new object with the transactions in the file
        """

       
        with open(infile, "r") as file:
            record_list = json.load(file)
            # create a list of sale objects from the file
            sales_list = [Sale(item['id'], item['name'], item['quantity'], item['price'], item['purchase_price'], item['timestamp'], item['customerID'], item['salesperson'], item['prescriptionID']) for item in record_list]
            

        # print(sales_list) 


        #TODO: Implement the function. Make sure to handle the cases where
        # the file does not exist.
        return BookRecords(sales_list)