class CustomSetIterator:
    def __init__(self, elements):
        self._elements = elements
        self._index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self._index < len(self._elements):
            result = self._elements[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration