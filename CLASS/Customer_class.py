# Define a class named Customer to represent customer information
class Customer:
    # Constructor method to initialize the customer object
    def __init__(self, name: str, address: str):
        # Initialize the name attribute of the customer
        self.name = name
        # Initialize the address attribute of the customer
        self.address = address

    # Special method to return a string representation of the customer object
    def __str__(self):
        # Return a formatted string containing the customer's name and address
        return f"Customer Information:\nName: {self.name}\nAddress: {self.address}"

# Check if the script is being run directly (not being imported as a module)
if __name__ == '__main__':
    # Create a new Customer object with name 'LAKICA LETICIA' and address 'KAMPALA'
    customer1 = Customer('LAKICA LETICIA', 'KAMPALA')
    # Print the customer's information using the __str__ method
    print(customer1)