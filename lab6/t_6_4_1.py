class CustomListIterator:
    def __init__(self, elements):
        odds = sorted([x for x in elements if x % 2 != 0])
        evens = sorted([x for x in elements if x % 2 == 0], reverse=True)
        self._sorted_items = odds + evens
        self._index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self._index < len(self._sorted_items):
            result = self._sorted_items[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

class CustomList:
    def __init__(self, elements_list):
        for el in elements_list:
            if not isinstance(el, int):
                raise ValueError(f"Елемент {el} не є цілим числом")
        self._items = list(elements_list)
    def __iter__(self):
        return CustomListIterator(self._items)
    def __getitem__(self, index):
        return self._items[index]
    def __setitem__(self, index, value):
        if not isinstance(value, int):
            raise ValueError("CustomList може містити лише цілі числа")
        self._items[index] = value
    def __len__(self):
        return len(self._items)
    def __contains__(self, value):
        return value in self._items
    def __iadd__(self, other):
        if isinstance(other, int):
            self._items.append(other)
        elif isinstance(other, CustomList):
            self._items.extend(other._items)
        else:
            raise TypeError(f"Додавати до списку можна лише ціле число або інший список. Ви намагаєтесь додати {type(other)}")
        return self
    def __isub__(self, other):
        if isinstance(other, int):
            elements_to_remove = [other]
        elif isinstance(other, CustomList):
            elements_to_remove = other._items
        else:
            raise TypeError(f"Видаляти зы списку можна лише ціле число або інший список. Ви намагаєтесь видалити {type(other)}")
        self._items = [x for x in self._items if x not in elements_to_remove]
        return self
    def __imul__(self, other):
        if isinstance(other, int):
            self._items *= other
        else:
            raise TypeError("Правим операндом *= має бути ціле число")
        return self
    def __sum__(self):
        return sum(self._items)
    def __str__(self):
        return str(self._items)

if __name__ == '__main__':
    filename = "test_numbers.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Ось кілька чисел для перевірки: 10, -3, 8, 5, 2, 9, -4, 7, 0, 11\n")
        file.write("А тут ще трохи: 14, 1, 6, 3")

    found_numbers = []
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()
        for word in text.split():
            clean_word = word.strip(",.:;!?")
            try:
                found_numbers.append(int(clean_word))
            except ValueError:
                continue

    custom_list = CustomList(found_numbers)

    print(f"Початковий список (як він зберігається в пам'яті):")
    print(custom_list)
    print("\n--- Результат роботи кастомного ітератора ---")
    for number in custom_list:
        print(number, end=" ")
    print()