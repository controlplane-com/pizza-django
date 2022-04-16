# fork from https://github.com/Magicjarvis/pizzapi
from pizzapy import ConsoleInput, StoreLocator, Customer


def main():
    print("####################")
    print(" Welcome to Dominos")
    print("####################")

    customer = ConsoleInput.get_customer()
    customer.save(customer.first_name + " " + customer.last_name)
    show_stores(customer, 5)
    card = ConsoleInput.get_credit_card()


def show_stores(customer, k):
    print("\nFinding Closest Stores...")
    print("\n- CLOSEST STORES -")
    k_local_dominos = StoreLocator.find_k_closest_stores_to_customer(customer, k)
    for i, store in enumerate(k_local_dominos):
        print(str(i+1) + ".")
        print(store)
        print()

if __name__ == "__main__":
    main()