from datetime import timedelta
from room import Room

class Hotel:
    def __init__(self,rooms):
        if isinstance(rooms, Hotel):
            self.rooms = [Room(r) for r in rooms.rooms]
        else:
            self.rooms = rooms

    @staticmethod
    def cost(room, guest):
        delta = guest.check_out - guest.check_in
        return delta.days*room.price

    def check_in(self, guest):
        for room in self.rooms:
            if room.is_free(guest.check_in, guest.check_out) and self.cost(room, guest) <= guest.budget:
                return room.occupy(guest)
        return False

    def free_rooms(self, start_day, end_day):
        count = 0
        for room in self.rooms:
            if room.is_free(start_day, end_day):
                count += 1
        return count

    def free_room(self, check_in, check_out):
        for room in self.rooms:
            if room.is_free(check_in, check_out):
                return room
        return None

    def profit(self, start_day, end_day):
        prof = 0
        while start_day < end_day:
            for room in self.rooms:
                if start_day in room.occupation:
                    prof += room.price
            start_day += timedelta(days=1)
        return prof

    def find_guest(self, guest):
        for room in self.rooms:
            if not room.is_free(guest.check_in, guest.check_out) and guest == room.occupation[guest.check_in]:
                return room
        return None