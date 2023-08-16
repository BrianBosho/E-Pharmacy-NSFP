import json

from typing import List, Dict, Union
from .product import Product


class Prescription:
    """Represents a prescription object

    Attributes:
        DoctorName: the name of the doctor who gave the prescription
        PrescriptionID: ID of the prescription
        Medications: list of the medications, this is the quantity, the ID, the name, and whether it was processed or not
        # see format in prescriptions.json
        CustomerID: ID of the customer
    """
    def __init__(self, DoctorName: str, PrescriptionID: str, Medications: List[Dict[str, Union[int, str, bool]]],
                 CustomerID: str, Date: str) -> None:
        self.DoctorName = DoctorName
        self.PrescriptionID = PrescriptionID
        self.Medications = Medications
        self.CustomerID = CustomerID

    def medecineInPrescription(self, product: Product, quantity: int) -> bool:
        """Verifies if a medecine with the specified quantity is included in a prescription

        Args:
            product: the product to verify
            quantity: the quantity to be added
        # read the prescription file and check if the product is in the prescription
        # check the quantity      

        Returns: A boolean denoting whether the value was found
        """
        #TODO: Implement the function
        # read items from medications list and check if the product is in the prescription and the quantity
        meds = self.Medications
        # find the products in the prescription
        for med in meds:
            if med['name'] == product.Name and med['quantity'] == quantity:
                return True
        return False
        
    def markComplete(self, product: Product):
        """Mark a product's sale complete in the prescriptions file

        Args:
            product: the product sold

        Returns: None
        """
        #TODO: Change the value "ProcessedStatus" of the relevant product to True
        meds = self.Medications
        for med in meds:
            if med['name'] == product.Name:
                med['ProcessedStatus'] = True

        # return NotImplemented

    def dump(self, outfile: str):
        """Dumps the updated prescription to the specified file
        
        Args: 
            outfile: path to the file where the output should be written

        Returns: None
        """
        #TODO: Read the output file (safely). 
        with open(outfile, 'r') as file:
            data = json.load(file)

        #TODO: Update the prescription that is being edited in the loaded data
        #identify the prescription to be updated
        for item in data:
            if item['PrescriptionID'] == self.PrescriptionID:
                item = {
                    "DoctorName": self.DoctorName,
                    "PrescriptionID": self.PrescriptionID,
                    "Medications": self.Medications,
                    "CustomerID": self.CustomerID,
                    "Date": self.Date
                    
                }
                break
        

        #TODO: Save the updated object
        with open(outfile, 'w') as file:
            json.dump(data, file)
    
    @classmethod
    def get(cls, infile: str, id: str):
        """Retrieves a specific prescription from a file
        
        Args:
            infile: path to the input file
            id: identifier of the prescription to add

        Returns: A prescription object as a dictionary
        """
        #TODO: Load the file and find the object with the relevant ID
        #TODO: Return the relevant prescription
        with open(infile, 'r') as file:
            data = json.load(file)
        for item in data:
            if item['PrescriptionID'] == id:
                return item
        return None
        
