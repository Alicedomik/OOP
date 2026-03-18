from pentagon import Pentagon
from hexagon import  Hexagon
from polygon import Polygon
def processing(filename):
    try:
        convex = []
        with open(filename) as f:
            for line in f:
                coords = [float(x) for x in line.split()]
                if len(coords) == 0:
                    continue
                elif len(coords) == 10:
                    pentagon = Pentagon(*coords)
                    if pentagon.is_convex(): convex.append(pentagon)
                elif len(coords) == 12:
                    hexagon = Hexagon(*coords)
                    if hexagon.is_convex(): convex.append(hexagon)
                else:
                    polygon = Polygon(*coords)
                    if polygon.is_convex(): convex.append(polygon)
            for i in range (0,len(convex)):
                print(f"{convex[i]} is convex")
    except FileNotFoundError:
        print("File not found")
    except ValueError:
        print("Value error")
processing("test")
