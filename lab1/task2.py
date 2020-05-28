import matplotlib.pyplot as plt
import numpy
import random
from Point import Point


point1 = Point(random.randint(0, 10), random.randint(0, 10))
point2 = Point(random.randint(0, 10), random.randint(0, 10))
point3 = Point(random.randint(0, 10), random.randint(0, 10))
point4 = Point(random.randint(0, 10), random.randint(0, 10))


def getMatrix(p1: Point, p2: Point, p3: Point):
    return [[p3.x - p2.x, p3.y - p2.y], [p1.x - p2.x, p1.y - p2.y]]


def areIntersect(matrices: list) -> str:
    d1 = numpy.linalg.det(matrices[0])
    d2 = numpy.linalg.det(matrices[1])
    d3 = numpy.linalg.det(matrices[2])
    d4 = numpy.linalg.det(matrices[3])

    if d1 == d2 and d2 == d3 and d3 == d4:
        return 'все точки лежат на одной прямой'
    elif d1 * d2 <= 0 and d3 * d4 <= 0:
        return 'пересекаются'
    else:
        return 'не пересекаются'


def drawLine(p1: Point, p2: Point):
    plt.plot([p1.x, p2.x], [p1.y, p2.y])


def drawText(text: str):
    plt.suptitle(text, fontsize=14)


def draw(p1: Point, p2: Point, p3: Point, p4: Point):
    matrices = [getMatrix(p1, p3, p4), getMatrix(p2, p3, p4), getMatrix(p1, p2, p3), getMatrix(p1, p2, p4)]
    plt.grid(True)    # линии вспомогательной сетки
    drawLine(p1, p2)
    drawLine(p3, p4)
    drawText(areIntersect(matrices))
    plt.show()


draw(point1, point2, point3, point4)



