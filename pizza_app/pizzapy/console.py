# fork from https://github.com/Magicjarvis/pizzapi

from pizzapy import Customer, StoreLocator, Order, CreditCard
from os import walk
from pathlib import Path

class ConsoleInput:
    """
    Used to get console input from users.
    """
    country = "US"

    @staticmethod
    def get_new_customer() -> Customer:
        """
        Collects information from console input and returns a new
        Customer object

        :return: Customer
        """
        print("-- PERSONAL INFORMATION --")
        print("To start an order you must provide the following details.\n")
        print("- COUNTRY -")
        is_canada = input("If you are ordering from Canada please type \"YES\" now: ")
        if is_canada.strip().upper() in ["YES","Y", "YA"]:
            ConsoleInput.country = "CA"

        print("\n- NAME -")
        first_name = ConsoleInput.get_valid_input("Please type your FIRST NAME: ", ConsoleInput.validate_name)
        last_name = ConsoleInput.get_valid_input("Please type your LAST NAME: ", ConsoleInput.validate_name)

        print("\n- CONTACT -")
        email = ConsoleInput.get_valid_input("Please type your EMAIL address: ", ConsoleInput.validate_email)
        phone = ConsoleInput.get_valid_input("Please type your PHONE NUMBER (no area code): ", ConsoleInput.validate_phone).replace("-","").replace("(", "").replace(")", "")

        print("\n- ADDRESS -")
        print("Please type your ADDRESS using the following form.")
        print("HOUSE #, Full Street Name, City, State/Province, ZIP/Postal Code")
        if ConsoleInput.country == "US":
            print("EXAMPLE: 700 Pennsylvania Avenue NW, Washington, DC, 20408")
        else:
            print("CANADA ADDRESS EXAMPLE: 100 Wellington St, Ottawa, ON, K1A0A9")

        address = ConsoleInput.get_valid_input("ADDRESS: ", ConsoleInput.validate_address)

        customer = Customer(last_name, first_name, email, phone, address)
        return customer

    @staticmethod
    def get_customer_files(path= str(Path(__file__).resolve().parents[1]) + "/customers"):
        f = []
        for (dirpath, dirnames, filenames) in walk(path):
            for file in filenames:
                f.append(dirpath + "/"+ file)

            break

        return f

    @staticmethod
    def load_customer(filename):
        return Customer.load(filename)

    @staticmethod
    def get_customer():
        new_customer = False
        customer_files = ConsoleInput.get_customer_files()

        if len(customer_files) == 0:
            print("No customer records exist, please make a new one.\n")
            new_customer = True
        else:
            returning = input("Would you like to load an exisiting custome profile? [y,n]: ")

            if returning.strip().lower() in ["y", "yes"]:
                customers = []
                for i in range(len(customer_files)):
                    cur_customer = ConsoleInput.load_customer(customer_files[i])
                    customers.append(cur_customer)
                    print(str(i+1) + ".")
                    print(cur_customer)

                while True:
                    ind = input("\nType the index of the entry you'd like to select: ")
                    if ind.isdigit():
                        ind = int(ind)
                        if 0 < ind <= len(customer_files):
                            customer = customers[ind-1]
                            break
                    else:
                        print("Invalid, try again.")

            else:
                new_customer = True

        if new_customer:
            customer = ConsoleInput.get_new_customer()

        return customer


    @staticmethod
    def get_valid_input(question:str, validation_function) -> str:
        """
        Will get valid input from the user and return it.

        :param validation_function: python function object used to validate input
        """
        while True:
            inp = input(question).strip()
            if validation_function(inp): break
            else:
                print("Invalid input, please try again.")

        return inp

    @staticmethod
    def validate_email(email:str) -> bool:
        """
        returns if the given email is valid
        """
        return email.count("@") == 1 and email.count(".") >= 1 and len(email) > 6

    @staticmethod
    def validate_address(address:str) -> bool:
        """
        returns if an address is valid
        """
        return True

    @staticmethod
    def validate_phone(phone:str) -> bool:
        """
        returns if the given phone number is valid
        """
        phone = phone.replace("-", "").replace("(", "").replace(")", "")
        return phone.isdigit() and len(phone) == 10

    @staticmethod
    def validate_name(name:str) -> bool:
        """
        a name is valid if it contains no spaces,
        no special chars and is longer than one character
        """
        return name.isalpha() and name.count(" ") == 0 and len(name) >= 2

    @staticmethod
    def get_credit_card() -> CreditCard:
        """
        gets a valid credit card from the user via console
        """
        print("- PAYMENT INFORMATION -")
        print("Please enter your credit card information. This information will NOT be saved.\n")
        card_number = input("Please type your CREDIT CARD NUMBER: ").strip()
        card_expiry= input("Please type the EXPIRY DATE (MM/YY): ").strip().replace("/","")
        cvv = input("Please type the 3 digit SECURITY CODE: ").strip()
        zip_code = input("Please type your ZIP/POSTAL CODE: ").strip()

        try:
            card = CreditCard(card_number, card_expiry, cvv, zip_code)
        except Exception as e:
            print("Card details INVALID, please try again. \n", e)
            return ConsoleInput.get_credit_card()

        return card
