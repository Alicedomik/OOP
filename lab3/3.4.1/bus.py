from car import Car
class Bus(Car):
    def __init__(self, fuel_consumption, capacity, fuel_in_tank, distance, max_passengers, ticket_price):
        super().__init__( fuel_consumption, capacity, fuel_in_tank, distance)
        self.max_passengers = max_passengers
        self.ticket_price = ticket_price
    def getEarn(self,distance =0, passengers=0):
            return self.ticket_price * passengers



