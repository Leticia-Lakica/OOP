# Define a class named Garage to represent a garage
class Garage:
    # Constructor method to initialize the garage object
    def __init__(self):
        # Initialize the vehicle attribute of the garage to None, indicating no vehicle is parked
        self.vehicle = None
    
    # Method to set a vehicle in the garage
    def setVehicle(self, Vehicle_parked):
        # Assign the Vehicle_parked object to the vehicle attribute of the garage
        self.vehicle = Vehicle_parked
        
    # Method to return a string representation of the garage, including the parked vehicle
    def toString(self):
        # Return a formatted string containing a description of the parked vehicle
        return f"Description of the parked vehicle: \n{self.vehicle.toString()}"