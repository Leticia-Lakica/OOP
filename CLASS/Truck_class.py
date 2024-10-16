# Import the Vehicle class from the vehicle module
from vehicle import Vehicle

# Define a class named Truck that inherits from the Vehicle class
class Truck(Vehicle):
    # Constructor method to initialize the Truck object with a color and an optional has_a_trailer parameter
    def __init__(self, color, has_a_trailer: bool = False):
        # Call the constructor of the parent Vehicle class to set the color
        super().__init__(color)
        
        # Initialize the has_a_trailer attribute of the Truck
        self.has_a_trailer = has_a_trailer
        
    # Method to return a string representation of the Truck
    def toString(self):
        # Return a formatted string describing the Truck's color and whether it has a trailer
        return f"This Vehicle is {self.getColor()}\nhas winter tire:{self.has_a_trailer}"
    
# Check if the script is being run directly (not being imported as a module)
if __name__ == '__main__':
    # Create a new Truck object with the color "Blue" and no trailer (default value)
    Truck1 = Truck("Blue")
    # Print the string representation of the truck using the toString method
    print(Truck1.toString())