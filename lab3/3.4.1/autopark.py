from personal import Personal
from truck import Truck
from bus import Bus
class Autopark:
    def __init__(self):
        self.cars = []
        self.failed_requests = []
        self.total_stats = {"distance": 0,
                            "earnings": 0,
                            "personal_passengers": 0,
                            "truck_weight": 0,
                            "personal_cars_used": 0,
                            "truck_cars_used": 0}
    def add_car(self, car_object):
        self.cars.append(car_object)
    def find_car(self, car_type, distance, load):
        can_carry = False
        can_drive_distance = False
        for car in self.cars:
            if car.is_used: continue
            if car_type == "Personal" and isinstance(car, Personal):
                if load <= car.max_passengers:
                    can_carry = True
                if distance <= car.distanceToRefill(load):
                    can_drive_distance = True
                if load <= car.max_passengers and distance <= car.distanceToRefill(load):
                    car.go(distance, load)
                    self.total_stats["personal_passengers"] += load
                    self.total_stats["earnings"] += car.getEarn(distance, load)
                    self.total_stats["distance"] += distance
                    self.total_stats["personal_cars_used"] += 1
                    return
            elif car_type == "Truck" and isinstance(car, Truck):
                if load <= car.max_load:
                    can_carry = True
                if distance <= car.distanceToRefill(load):
                    can_drive_distance = True
                if load <= car.max_load and distance <= car.distanceToRefill(load):
                    car.go(distance, load)
                    self.total_stats["truck_weight"] += load
                    self.total_stats["earnings"] += car.getEarn(distance, load)
                    self.total_stats["distance"] += distance
                    self.total_stats["truck_cars_used"] += 1
                    return
            elif car_type == "Bus" and isinstance(car, Bus):
                if load <= car.max_passengers:
                    can_carry = True
                if distance <= car.distanceToRefill(load):
                    can_drive_distance = True
                if load <= car.max_passengers and distance <= car.distanceToRefill(load):
                    car.go(distance, load)
                    self.total_stats["earnings"] += car.getEarn(distance, load)
                    self.total_stats["distance"] += distance
                    return

        request_info = f"[{car_type}, відстань: {distance}км, вантаж/люди: {load}]"
        if  can_carry and can_drive_distance:
            reason = f"Запит {request_info} відхилено: Усі автомобілі зайняті"
        elif not can_carry:
            reason = f"Запит {request_info} відхилено: Немає {car_type} з місткістю {load}"
        elif not can_drive_distance:
            reason = f"Запит {request_info} відхилено: Недостатньо палива в жодній {car_type} для дистанції {distance}"
        else:
            reason = "Невідома помилка"
        self.failed_requests.append(reason)