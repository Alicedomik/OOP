import math
class Vector:
    def __init__(self, *args):
        if len(args) == 1:
            arg = args[0]
            if isinstance(arg, Vector):
                self.coords = tuple(arg.coords)
            else:
                self.coords = (arg,)
        else:
            self.coords = args

    def __repr__(self):
        return f"V{self.coords}"

    def dimension(self):
        return len(self.coords)

    def length(self):
        return math.sqrt(sum(x ** 2 for x in self.coords))

    def arithmetic_mean(self):
        return sum(self.coords) / self.dimension()

    def minimum(self):
        return min(self.coords)

    def maximum(self):
        return max(self.coords)


def analyze_vectors(lines):
    dim_vectors = {}
    len_vectors = {}
    max_coords = {}
    min_coords = {}
    suma = 0
    number = 0
    for line in lines:
        coords = line.split()
        if not coords :
            continue
        try:
            vector = Vector(*map(float, coords))
            d = vector.dimension()
            if d == 0:
                continue
            if d in dim_vectors:
                dim_vectors[d].append(vector)
            else:
                dim_vectors[d] = [vector]

            l = round(vector.length(),6)
            if l in len_vectors:
                len_vectors[l].append(vector)
            else:
                len_vectors[l] = [vector]

            suma += l
            number += 1

            max_coord = vector.maximum()
            if max_coord in max_coords:
                max_coords[max_coord].append(vector)
            else:
                max_coords[max_coord] = [vector]

            min_coord = vector.minimum()
            if min_coord in min_coords:
                min_coords[min_coord].append(vector)
            else:
                min_coords[min_coord] = [vector]
        except ValueError:
            continue

    max_dim = max(dim_vectors.keys())
    candidates = dim_vectors[max_dim]
    if len(dim_vectors[max_dim]) == 1:
        print(f"Вектор з найбільшою розмірністю: {dim_vectors[max_dim][0]}")

    else:
        result = min(candidates, key=lambda v: v.length())
        print(f"Вектор з найбільшою розмірністю :{result}")

    max_len = max(len_vectors.keys())
    candidates = len_vectors[max_len]
    if len(len_vectors[max_len]) == 1:
        print(f"Вектор з найбільшою довжиною: {len_vectors[max_len][0]}")
    else:
        result = min(candidates, key=lambda v: v.dimension())
        print(f"Вектор з найбільшою довжиною: {result}")
    mid_len = suma/number
    print(f"Середня довжина вектора = {mid_len}")
    counter = 0
    for k, v in len_vectors.items():
        if k > mid_len:
            counter += len(v)
    print(f"Кількість векторів, які мають довжину більшу за середню = {counter}")

    max_c = max(max_coords.keys())
    candidates = max_coords[max_c]
    if len(max_coords[max_c]) == 1:
        print(f"Вектор з максимальною найбільшою компонентою: {max_coords[max_c][0]}")
    else:
        result = min(candidates, key=lambda v: v.minimum())
        print(f"Вектор з максимальною найбільшою компонентою: {result}")

    min_c = min(min_coords.keys())
    candidates = min_coords[min_c]
    if len(min_coords[min_c]) == 1:
        print(f"Вектор з мінімальною найменшою компонентою: {min_coords[min_c][0]}")
    else:
        result = max(candidates, key=lambda v: v.maximum())
        print(f"Вектор з мінімальною найменшою компонентою: {result}")


def get_keyboard_input():
    print("Вводьте координати векторів ")
    print("Щоб закінчити введення, натисніть Enter на порожньому рядку")
    lines = []
    while True:
        line = input(f"Рядок {len(lines) + 1}: ").strip()
        if not line:
            break
        lines.append(line)
    return lines

def main():
    choice = input("Звідки взяти дані? (1 - Файл, 2 - Клавіатура): ")

    if choice == "1":
        filename = input("Введіть назву файлу: ")
        try:
            with open(filename, 'r') as f:
                lines = f.readlines()
            analyze_vectors(lines)
        except FileNotFoundError:
            print("Файл не знайдено.")

    elif choice == "2":
        lines = get_keyboard_input()
        if lines:
            analyze_vectors(lines)
        else:
            print("Дані не введено.")
    else:
        print("Неправильний вибір.")


if __name__ == "__main__":
    main()
