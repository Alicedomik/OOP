from datetime import date
class Guest:
    def __init__(self, name, check_in: date, check_out: date, budget):
        if isinstance(name, Guest):
            self.name = name.name
            self.check_in = name.check_in
            self.check_out = name.check_out
            self.budget = name.budget
        else:
            self.name = name
            self.check_in = check_in
            self.check_out = check_out
            self.budget = budget

    def __str__(self):
        return self.name