class Hexagon:
    def __init__(self, *coords):
        if len(coords) == 1 :
            self.points = list(coords[0].points)
        elif len(coords) == 12:
            self.points = [(coords[i], coords[i + 1]) for i in range(0, 12, 2)]

    def __str__(self):
        return f"{self.__class__.__name__}({self.points})"

    def is_convex(self):
        prev_sign = 0
        for i in range(6):
            p1 = self.points[i]
            p2 = self.points[(i + 1) % 6]
            p3 = self.points[(i + 2) % 6]
            val = (p2[0] - p1[0]) * (p3[1] - p2[1]) - (p2[1] - p1[1]) * (p3[0] - p2[0])
            if val != 0:
                current_sign = 1 if val > 0 else -1
                if prev_sign == 0:
                    prev_sign = current_sign
                elif current_sign != prev_sign:
                    return False

        return True