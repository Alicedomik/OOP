from abc import ABC, abstractmethod
import os

class Student(ABC):
    def __init__(self, target_credits, initial_money):
        self.target_credits = target_credits
        self.money = initial_money
        self.credits = 0
        self.expelled = False

    @abstractmethod
    def accept(self, visitor):
        pass

    def can_get_diploma(self):
        return not self.expelled and self.credits >= self.target_credits


class HumanitarianStudent(Student):
    def accept(self, visitor):
        visitor.visit_humanitarian(self)


class NaturalStudent(Student):
    def accept(self, visitor):
        visitor.visit_natural(self)


class NaturalHumanStudent(Student):
    def accept(self, visitor):
        visitor.visit_natural_human(self)

class Visitor(ABC):
    @abstractmethod
    def visit_humanitarian(self, student): pass

    @abstractmethod
    def visit_natural(self, student): pass

    @abstractmethod
    def visit_natural_human(self, student): pass


class HumanitarianTeacher(Visitor):
    def __init__(self, credits_value):
        self.credits_value = credits_value

    def visit_humanitarian(self, student):
        student.credits += self.credits_value

    def visit_natural(self, student):
        pass

    def visit_natural_human(self, student):
        student.credits += self.credits_value


class NaturalTeacher(Visitor):
    def __init__(self, credits_value):
        self.credits_value = credits_value

    def visit_humanitarian(self, student):
        pass

    def visit_natural(self, student):
        student.credits += self.credits_value

    def visit_natural_human(self, student):
        student.credits += self.credits_value


class FinancialVisitor(Visitor):
    def visit_humanitarian(self, student):
        self.process(student)

    def visit_natural(self, student):
        self.process(student)

    def visit_natural_human(self, student):
        self.process(student)

    @abstractmethod
    def process(self, student):
        pass


class HostelVisitor(FinancialVisitor):
    def __init__(self, cost):
        self.cost = cost

    def process(self, student):
        if student.money >= self.cost:
            student.money -= self.cost
        else:
            student.expelled = True


class FoodVisitor(FinancialVisitor):
    def __init__(self, cost):
        self.cost = cost

    def process(self, student):
        if student.money >= self.cost:
            student.money -= self.cost
        else:
            student.expelled = True


class AccountingVisitor(FinancialVisitor):
    def __init__(self, amount):
        self.amount = amount

    def process(self, student):
        student.money += self.amount


class ParentsVisitor(FinancialVisitor):
    def __init__(self, amount):
        self.amount = amount

    def process(self, student):
        student.money += self.amount


def process_student_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = [line.strip().lower() for line in f if line.strip()]

    if len(lines) < 3:
        print(f"Помилка формату у файлі {file_path}")
        return False

    direction = lines[0]
    target_credits = int(lines[1])
    initial_money = int(lines[2])

    if direction in ('humanitarian', 'гуманітарний'):
        student = HumanitarianStudent(target_credits, initial_money)
    elif direction in ('natural', 'природничий'):
        student = NaturalStudent(target_credits, initial_money)
    elif direction in ('natural-humanitarian', 'природничо-гуманітарний'):
        student = NaturalHumanStudent(target_credits, initial_money)
    else:
        print(f"Невідомий напрям: {direction}")
        return False

    for line in lines[3:]:
        if student.expelled:
            break

        parts = line.split()
        if not parts:
            continue

        action = parts[0]
        amount = int(parts[-1])

        visitor = None
        if action == 'teach':
            subject = parts[1]
            if subject == 'humanitarian':
                visitor = HumanitarianTeacher(amount)
            elif subject == 'natural':
                visitor = NaturalTeacher(amount)

        elif action == 'pay':
            target = parts[1]
            if target == 'hostel':
                visitor = HostelVisitor(amount)
            elif target == 'food':
                visitor = FoodVisitor(amount)

        elif action == 'obtain':
            source = parts[1]
            if source == 'scholarship':
                visitor = AccountingVisitor(amount)
            elif source == 'parents':
                visitor = ParentsVisitor(amount)

        if visitor:
            student.accept(visitor)

    return student.can_get_diploma()


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    for i in range(1, 15):
        filename = f"input{i:02d}.txt"
        full_path = os.path.join(script_dir, filename)
        if os.path.exists(full_path):
            result = process_student_file(full_path)
            status = "ОТРИМАВ ДИПЛОМ" if result else "НЕ ОТРИМАВ ДИПЛОМУ (або відрахований)"
            print(f"Студент з файлу {filename}: {status}")
        else:
            print(f"Файл не знайдено: {full_path}")