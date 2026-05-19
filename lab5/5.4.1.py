class CustomList:
    def __init__(self, elements_list):
        for el in elements_list:
            if not isinstance(el, int):
                raise ValueError(f"Елемент {el} не є цілим числом")
        self._items = list(elements_list)
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
    text = ("натуральні числа: 3 8 36 4567 29, "
           "від'ємні числа: -10 -4 -458 -37, "
           "нуль: 0, "
           "раціональні числа: 1.5, 67.44, 536.19")
    found_numbers = []
    for word in text.split():
        clean_word = word.strip(",.:;!?")
        try:
            found_numbers.append(int(clean_word))
        except ValueError:
            continue
    custom_list = CustomList(found_numbers)
    print(f"Список цілих чисел: {custom_list}")
    print(f"Кількість: {len(custom_list)}")
    print(f"Сума: {sum(custom_list._items)}")
    f = False
    for el in custom_list:
        if el in {1,3,1984,7777}:
            f = True
            break
    if f: print("У тексті трапляється одне або декілька чисел з {1,3,1984,7777}")
    else: print("У тексті не трапляється хоча б одне з чисел {1,3,1984,7777}")
    new_list = []
    for el in custom_list:
        if el != 0:
            new_list.append(el)
    c_list = CustomList(new_list)
    print(f"Текст містить {len(c_list)} цілих чисел")

