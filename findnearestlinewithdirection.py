from shapely.geometry import Point
import math

point = (0, 0)
angle = 180
lines = [((1, -1), (1, 1)), ((2, -1), (2, 1))]
data = []
dictionary = {}


def intersection(O, P, A, B, line):
    try:
        line_found = False
        a1 = B.y - A.y
        b1 = A.x - B.x
        c1 = a1 * A.x + b1 * A.y
        a2 = P.y - O.y
        b2 = O.x - P.x
        c2 = a2 * O.x + b2 * O.y

        determinant = a1 * b2 - a2 * b1
        if determinant == 0:
            return Point(10 * 9, 10 * 9), line_found
        else:
            x = round(((b2 * c1 - b1 * c2) / determinant), 2)
            y = round(((a1 * c2 - a2 * c1) / determinant), 2)

        x1, y1 = point
        x2, y2 = (x, y)
        distance = calculateDistance(x1, y1, x2, y2)
        data.append(distance)
        dict = {distance: line}
        dictionary.update(dict)
        return
    except Exception as e:
        print("Oops!", e.__class__, "some error occurred.")


def calculateDistance(x1, y1, x2, y2):
    try:
        dist = math.sqrt((x2 - x1) * 2 + (y2 - y1) * 2)
        return dist
    except Exception as e:
        print("Oops!", e.__class__, "some error occurred.")


def closestline(dictionary):
    try:
        for i in data:
            if i == min(data):
                return dictionary.get(i)
        else:
            return "Doesn't Intersect !!!"
    except Exception as e:
        print("Oops!", e.__class__, "some error occurred.")


def findlinesegment(angle, lines):
    try:

        origin = (0, 0)
        start = Point(origin)
        length = 10000
        end = Point(start.x + length * math.cos(angle), start.y + length * math.sin(angle))
        for p in lines:
            st, en = p
            st = Point(st)
            en = Point(en)
            intersection(start, end, st, en, p)

        print(
            f'The closest line segment to the point {point} at an angle of {angle} degree : {closestline(dictionary)}.')
    except Exception as e:
        print("Oops!", e.__class__, "some error occurred.")


if __name__ == "__main__":
    findlinesegment(0, [((9, -1), (1, 1)), ((2, -1), (2, 1))])
