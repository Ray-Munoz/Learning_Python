# Create a vehicle class with max_speed and mileage attributes

class vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


# modelX example
modelX = vehicle('Tesla',240, 18)
print(modelX.name, modelX.max_speed, modelX.mileage)

class bus(vehicle):
    pass
school_vehicle = bus('School-Bus', 140, 10)
print(school_vehicle.name, school_vehicle.max_speed, school_vehicle.mileage)
