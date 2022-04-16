from .address import Address
import json

class Customer:
    """The Customer who orders a pizza."""

    def __init__(self, fname='', lname='', email='', phone='', address=None):
        self.first_name = fname.strip()
        self.last_name = lname.strip()
        self.email = email.strip()
        self.phone = str(phone).strip()
        self.str_address = address
        self.address = Address(*address.split(','))

    def save(self, filename="customers/customer1.json"):
        """
        saves the current customer to a .json file for loading later
        """
        if not filename.startswith("customers"):
            filename = "customers/" + filename
        json_dict = {"first_name": self.first_name,
             "last_name": self.last_name,
             "email": self.email,
             "phone": self.phone,
             "address": self.str_address}

        with open(filename, "w") as f:
            json.dump(json_dict, f)

    @staticmethod
    def load(filename):
        """
        load and return a new customer object from a json file
        """
        with open(filename, "r") as f:
            data = json.load(f)

            customer = Customer(data["first_name"], 
                                data["last_name"],
                                data["email"],
                                data["phone"],
                                data["address"])
        return customer

    def __repr__(self):
        return "Name: {} {}\nEmail: {}\nPhone: {}\nAddress: {}".format(
            self.first_name,
            self.last_name,
            self.email,
            self.phone,
            self.address,
        )
