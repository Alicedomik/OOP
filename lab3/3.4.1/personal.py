from car import Car
class Personal(Car):
    def __init__(self, fuel_consumption, capacity, fuel_in_tank, distance, max_passengers, cost_taxi):
        super().__init__(fuel_consumption, capacity, fuel_in_tank, distance)
        self.max_passengers = max_passengers
        self.cost_taxi = cost_taxi
    def fuelPerKm(self, passengers=0):
        return self.fuel_consumption*(1+0.1*passengers)
    def costKm(self, passengers=0):
        return self.cost_taxi

