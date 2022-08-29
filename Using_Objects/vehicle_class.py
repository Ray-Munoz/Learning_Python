# Create a vehicle class with max_speed and mileage attributes

class vehicle:
    def __init__(self, name, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.name = name

# modelX example
modelX = vehicle(240, 18)
print(modelX.max_speed, modelX.mileage)
