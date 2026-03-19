class Polygon:
    def __init__(self, *coords):
        if len(coords) == 1:
            self.points = coords[0].points
        else:
            self.points = [(coords[i], coords[i + 1]) for i in range(0, len(coords), 2)]

    def __str__(self):
        return f"{self.__class__.__name__}({self.points})"

    def is_convex(self):
        n = len(self.points)
        if n < 3:
            return False

        prev_sign = 0
        for i in range(n):
            p1 = self.points[i]
            p2 = self.points[(i + 1) % n]
            p3 = self.points[(i + 2) % n]
            val = (p2[0] - p1[0]) * (p3[1] - p2[1]) - (p2[1] - p1[1]) * (p3[0] - p2[0])
            if val != 0:
                current_sign = 1 if val > 0 else -1
                if prev_sign == 0:
                    prev_sign = current_sign
                elif current_sign != prev_sign:
                    return False

        return True