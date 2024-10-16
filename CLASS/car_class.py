# Import the Vehicle class from the vehicle module
from vehicle import Vehicle

# Define a class named Car that inherits from the Vehicle class
class Car(Vehicle):
    # Constructor method to initialize the Car object with a color and an optional has_winter_tires parameter
    def __init__(self, color, has_winter_tires: bool = False):
        # Call the constructor of the parent Vehicle class to set the color
        super().__init__(color)
        
        # Initialize the has_winter_tires attribute of the Car
        self.has_winter_tires = has_winter_tires
        
    # Method to return a string representation of the Car
    def toString(self):
        # Return a formatted string describing the Car's color and whether it has winter tires
        return f"This Vehicle is {self.getColor()}\nhas winter tire:{self.has_winter_tires}"

# Check if the script is being run directly
if __name__ == '__main__':
    # Create a new Car object with the color "Blue" and no winter tires 
    car1 = Car("Blue")
    # Print the string representation of the car using the toString method
    print(car1.toString())