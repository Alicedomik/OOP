from car import Car
class Truck(Car):
    def __init__(self, fuel_consumption, capacity, fuel_in_tank, distance, max_load, cost_for_ton):
        super().__init__(fuel_consumption, capacity, fuel_in_tank, distance)
        self.max_load = max_load
        self.cost_for_ton = cost_for_ton
    def fuelPerKm(self, tons=0):
        return self.fuel_consumption*(1+0.25*tons)
    def costKm(self, tons=0):
        return self.cost_for_ton*tons
