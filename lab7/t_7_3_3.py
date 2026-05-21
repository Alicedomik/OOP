from t_7_3_1 import Rational
from t_7_3_2 import RationalValueError

class RationalList:
    def __init__(self, elements=None):
        self._data = []
        if elements:
            for item in elements:
                self.append(item)

    def append(self, item):
        if not isinstance(item, Rational):
            raise RationalValueError("Елементом RationalList може бути лише об'єкт класу Rational")
        self._data.append(item)

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        if not isinstance(value, Rational):
            raise TypeError("Значення має бути об'єктом Rational")
        self._data[index] = value

    def __len__(self):
        return len(self._data)

    def __add__(self, other):
        new_list = RationalList(self._data)
        if isinstance(other, RationalList):
            new_list._data.extend(other._data)
        elif isinstance(other, (Rational, int)):
            item = other if isinstance(other, Rational) else Rational(other)
            new_list.append(item)
        else:
            return NotImplemented
        return new_list

    def __iadd__(self, other):
        if isinstance(other, RationalList):
            self._data.extend(other._data)
        elif isinstance(other, (Rational, int)):
            item = other if isinstance(other, Rational) else Rational(other)
            self.append(item)
        else:
            return NotImplemented
        return self

    def sum_all(self):
        res = Rational(0)
        for item in self._data:
            res += item
        return res