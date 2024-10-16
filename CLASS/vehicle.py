class Vehicle:
    def __init__(self, color):
        #Initializes the Vehicle with a color.
        self.color = color

    def getColor(self):
        #Returns the color of the Vehicle.
        return self.color

    def toString(self):
        #Returns a string representation of the Vehicle.
        return f"This vehicle is {self.color}"


if __name__ == '__main__':
    vehicle1 = Vehicle("red")
    print(vehicle1.getColor())  #Output: red
    print(vehicle1.toString())  # Output:The vehicle is red
            

    