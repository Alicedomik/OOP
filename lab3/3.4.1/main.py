from personal import Personal
from truck import Truck
from bus import Bus
from autopark import  Autopark

def setup_autopark():
    park = Autopark()
    park.add_car(Personal(fuel_consumption=8, capacity=50, fuel_in_tank=60, distance=0, max_passengers=4, cost_taxi=15))
    park.add_car(Truck(fuel_consumption=25, capacity=300, fuel_in_tank=150, distance=0, max_load=10, cost_for_ton=50))
    park.add_car(Bus(fuel_consumption=30, capacity=200, fuel_in_tank=100, distance=0, max_passengers=50, ticket_price=120))
    park.add_car(Personal(fuel_consumption=8, capacity=50, fuel_in_tank=60, distance=0, max_passengers=4, cost_taxi=15))
    park.add_car(Truck(fuel_consumption=25, capacity=300, fuel_in_tank=150, distance=0, max_load=10, cost_for_ton=50))
    park.add_car(Bus(fuel_consumption=30, capacity=200, fuel_in_tank=100, distance=0, max_passengers=50, ticket_price=120))
    park.add_car(Personal(fuel_consumption=8, capacity=50, fuel_in_tank=60, distance=0, max_passengers=4, cost_taxi=15))
    park.add_car(Truck(fuel_consumption=25, capacity=300, fuel_in_tank=150, distance=0, max_load=10, cost_for_ton=50))
    park.add_car(Bus(fuel_consumption=30, capacity=200, fuel_in_tank=100, distance=0, max_passengers=50, ticket_price=120))
    return park

def processing(filename):
    autopark = setup_autopark()
    try:
        with open(filename) as f:
            for line in f:
                car_type, distance, load = line.strip().split()
                distance, load = float(distance), float(load)
                autopark.find_car(car_type, distance, load)
    except FileNotFoundError:
        print("Файл не знайдено")

    print("------Обробка файлу------")
    print(f"1.{'Так' if not autopark.failed_requests else 'Ні'}")
    if autopark.failed_requests:
        with open('failed_requests.txt', 'w', encoding='utf-8') as f:
            for error in autopark.failed_requests:
                f.write(error + "\n")
    print(f"2. Загальна відстань: {autopark.total_stats['distance']} км")
    print(f"3. Всього пасажирів (легкові): {autopark.total_stats['personal_passengers']}")
    avg_pass = autopark.total_stats['personal_passengers'] / autopark.total_stats['personal_cars_used'] if autopark.total_stats['personal_cars_used'] > 0 else 0
    print(f"4. Середньо пасажирів на легковик: {avg_pass:.2f}")
    print(f"5. Всього вантажу: {autopark.total_stats['truck_weight']} тонн")
    avg_load = autopark.total_stats['truck_weight'] / autopark.total_stats['truck_cars_used'] if autopark.total_stats['truck_cars_used'] > 0 else 0
    print(f"6. Середня вага на вантажівку: {avg_load:.2f} т")
    print(f"7. Загальний заробіток автобази: {autopark.total_stats['earnings']:.2f} грн")


if __name__ == "__main__":
    processing("test.txt")