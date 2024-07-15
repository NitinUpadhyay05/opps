# Define a global variable traffic_light
traffic_light = "Green"

# Define a module-level variable speed_limit
speed_limit = 60

class Vehicle:
    def start_engine(self):
        message = "Engine started."  
        print(message)

class Car(Vehicle):
    def __init__(self, make):
        self.make = make  
    
    def start_engine(self):
        message = "Car engine started." 
        print(message)

class Bike(Vehicle):
    def __init__(self, bike_type):
        self.type = bike_type  
    
    def start_engine(self):
        message = "Bike engine started."  
        print(message)

# Creating each start_engine method
my_vehicle = Vehicle()
my_car = Car("Toyota")
my_bike = Bike("Mountain")

# Call the start_engine method 
my_vehicle.start_engine()
my_car.start_engine()
my_bike.start_engine()

# Print global and module-level variables
print(f"Traffic light: {traffic_light}")
print(f"Speed limit: {speed_limit}")
