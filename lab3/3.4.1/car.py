class Car:
    def __init__(self, fuel_consumption, capacity, fuel_in_tank, distance):
        self.fuel_consumption = fuel_consumption/100
        self.capacity = capacity
        self.fuel_in_tank = fuel_in_tank
        self.distance = distance
        self.is_used = False
    def go(self, distance, load=0):
        self.distance += distance
        self.fuel_in_tank -= distance * self.fuelPerKm(load)
        self.is_used = True
    def distanceToRefill(self, load=0):
        return self.fuel_in_tank / self.fuelPerKm(load)
    def getEarn(self, distance, load=0):
        return distance * self.costKm(load)
    def fuelPerKm(self, load=0):
        return self.fuel_consumption
    def costKm(self, load=0):
        pass