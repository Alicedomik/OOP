from datetime import date
from lab1.guest import Guest
from lab1.room import Room
from lab1.hotel import Hotel

rooms =[Room(101, 500, "standard"),
        Room(102, 500, "standard"),
        Room(103, 500, "standard"),
        Room(201, 1000, "luxury"),
        Room(202, 1000, "luxury")]

hotel = Hotel(rooms)
check_in = date(2026, 3,12)
check_out = date(2026, 3,20)

guest = Guest("Josh Martin", date(2026,7, 13), date(2026, 8, 16), 50000)

print(f"На період з {check_in} по {check_out} є {hotel.free_rooms(check_in, check_out)} вільних кімнат")
print(f"На період з {check_in} по {check_out} є вільна кімната {hotel.free_room(check_in, check_out)}")
if hotel.check_in(guest):
    print(f"Жильця {guest} успішно поселено в кімнату {hotel.find_guest(guest)}")
else:
    print(f"Ми не змогли знайті підходящу кімнату для жильця {guest}")
print(f"Вартість проживання жильця {guest} у період з {guest.check_in} по {guest.check_out} сягатиме {hotel.cost(hotel.find_guest(guest), guest)}")
print(f"У період з {check_in} по {check_out} готель заробить {hotel.profit(check_in, check_out)}")
