from datetime import timedelta
class Room:
    def __init__(self, number, price=None, type_=None):
        if isinstance(number, Room):
            self.number = number.number
            self.price = number.price
            self.type_ = number.type_
            self.occupation = number.occupation.copy()
        else:
            self.number = number
            self.price = price
            self.type_ = type_
            self.occupation = {}

    def is_free(self, check_in, check_out):
        while check_in < check_out:
            if check_in in self.occupation:
                return False
            check_in += timedelta(days=1)
        return True

    def occupy(self, guest):
        if self.is_free(guest.check_in, guest.check_out):
            current_day = guest.check_in
            while current_day < guest.check_out:
                self.occupation[current_day] = guest
                current_day += timedelta(days=1)
            return True
        return False

    def __str__(self):
        return f'номер {self.number}'