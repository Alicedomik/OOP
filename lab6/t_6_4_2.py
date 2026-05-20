class Segment:
    def __init__(self, start, end):
        self.start = min(start, end)
        self.end = max(start, end)

class SegmentSetIterator:
    def __init__(self, segments):
        self._sorted_segments = sorted(segments, key=lambda s: (s.start, s.end))
        self._index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self._index < len(self._sorted_segments):
            result = self._sorted_segments[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration
