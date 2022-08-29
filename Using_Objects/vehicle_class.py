# Create a vehicle class with max_speed and mileage attributes

class vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

# modelX example
modelX = vehicle(240, 18)
print(modelX.max_speed, modelX.mileage)
