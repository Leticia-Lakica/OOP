from Garage_class import Garage
from Truck_class import Truck

# Import the Garage class from the Garage_class module
from Garage_class import Garage
# Import the Truck class from the Truck_class module
from Truck_class import Truck

# Define a new class called Garage_tester that inherits from the Garage class
class Garage_tester(Garage):
    # Initialize the Garage_tester class
    def __init__(self):
        # Call the constructor of the parent class (Garage) using super()
        super().__init__()
        
    # Define a method to get an example of how to use the Garage class
    def getExample(self):
        # Create a new Truck object with color 'black' and False for some other attribute (likely indicating whether it's in use or not)
        truck = Truck('black', False)
        
        # Create a new Garage object
        my_garage = Garage()
        
        # Set the vehicle in the garage to the truck we created earlier
        my_garage.setVehicle(truck)
        
        # Print a string representation of the garage
        print(my_garage.toString())
        
# Check if this script is being run directly (not being imported as a module in another script)
if __name__ == '__main__':
    # Create a new Garage_tester object and call its getExample method
    Garage_tester().getExample()
        
        
    