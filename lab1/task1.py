import matplotlib.pyplot as plt
import numpy
import random
from Point import Point


point0 = Point(random.randint(0, 10), random.randint(0, 10))
point1 = Point(random.randint(0, 10), random.randint(0, 10))
point2 = Point(random.randint(0, 10), random.randint(0, 10))


def getMatrix(p0: Point, p1: Point, p2: Point):
    return [[p2.x - p1.x, p2.y - p1.y], [p0.x - p1.x, p0.y - p1.y]]


def getPointPosition(matrix: list) -> str:
    d = numpy.linalg.det(matrix)
    if d > 0:
        return 'left'
    elif d < 0:
        return 'right'
    else:
        return 'on the line'


def drawLine(p1: Point, p2: Point):
    plt.plot([0, p1.x, p2.x], [0, p1.y, p2.y])


def drawPoint(p0: Point):
    plt.scatter(p0.x, p0.y)


def drawText(text: str):
    plt.suptitle(text, fontsize=14)


def draw(p0: Point, p1: Point, p2: Point):
    plt.grid(True)    # линии вспомогательной сетки
    drawLine(p1, p2)
    drawPoint(p0)
    drawText(getPointPosition(getMatrix(point0, point1, point2)))
    plt.show()


draw(point0, point1, point2)



