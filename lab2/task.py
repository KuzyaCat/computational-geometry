import matplotlib.pyplot as plt
from Point import Point
import random


def initPoints(xs: list, ys: list) -> list:
    points = []
    for i in range(len(xs)):
        x = Point(xs[i], ys[i])
        points.append(x)
    return points


def drawPolygon(points: list):
    for i in range(len(points) - 1):
        plt.plot([points[i].x, points[i + 1].x], [points[i].y, points[i + 1].y])


def drawPoint(point: Point):
    plt.scatter(point.x, point.y)


def drawLine(p1: Point, p2: Point):
    plt.plot([p1.x, p2.x], [p1.y, p2.y])


def det(a, b, c, d):
    return a * d - b * c


def areIntersect(p1: Point, p2: Point, p3: Point, p4: Point) -> bool:
    d1 = det(p4.x - p3.x, p4.y - p3.y, p1.x - p3.x, p1.y - p3.y)
    d2 = det(p4.x - p3.x, p4.y - p3.y, p2.x - p3.x, p2.y - p3.y)
    d3 = det(p2.x - p1.x, p2.y - p1.y, p3.x - p1.x, p3.y - p1.y)
    d4 = det(p2.x - p1.x, p2.y - p1.y, p4.x - p1.x, p4.y - p1.y)

    if d1 * d2 <= 0 and d3 * d4 <= 0:
        return True
    else:
        return False


def getPointPositionToLine(p0: Point, p1: Point, p2: Point) -> str:
    d = det(p2.x - p1.x, p2.y - p1.y, p0.x - p1.x, p0.y - p1.y)
    if d > 0:
        return 'left'
    elif d < 0:
        return 'right'
    else:
        return 'on the line'


def lineOnPolygonBound(p0: Point, points: list) -> bool:
    for i in range(len(points) - 1):
        # print('i: ', i, ' ::: ', points[i].x, ' ::: ', points[i].y, ' ::: ', points[i + 1].x, ' ::: ', points[i + 1].y)
        # print(getPointPositionToLine(p0, points[i], points[i + 1]))
        if getPointPositionToLine(p0, points[i], points[i + 1]) == 'on the line':
            return True
    return False


def overallTest(initialPoint: Point, points: Point) -> bool:
    minX = points[0].x
    minY = points[0].y
    maxX = points[0].x
    maxY = points[0].y
    for i in range(len(points)):
        if (points[i].x > maxX):
            maxX = points[i].x
        if (points[i].x < minX):
            minX = points[i].x
        if (points[i].y > maxY):
            maxY = points[i].y
        if (points[i].y < minY):
            minY = points[i].y

    if initialPoint.x < minX or initialPoint.x > maxX or initialPoint.y < minY or initialPoint.y > maxY:
        return False
    else:
        return True


def getMinX(points: list):
    minX = points[0].x
    for i in range(len(points)):
        if (points[i].x < minX):
            minX = points[i].x
    return minX


def radialTest(initialPoint: Point, points: list) -> bool:
    if not overallTest(initialPoint, points):
        return False

    q = Point(getMinX(points) - 1, initialPoint.y)
    s = 0

    for i in range(len(points) - 1):
        if areIntersect(points[i], points[i + 1], q, initialPoint):
            if (not getPointPositionToLine(points[i], q, initialPoint) == 'on the line' and
                    not getPointPositionToLine(points[i + 1], q, initialPoint) == 'on the line'):
                s += 1
            elif getPointPositionToLine(points[i], q, initialPoint) == 'on the line':
                k = 0
                while getPointPositionToLine(points[i + k], q, initialPoint) == 'on the line':
                    k += 1
                if (not getPointPositionToLine(points[i - 1], q, initialPoint) ==
                        getPointPositionToLine(points[i + k], q, initialPoint) and
                        not getPointPositionToLine(points[i - 1], q, initialPoint) == 'on the line' and
                        not getPointPositionToLine(points[i + k], q, initialPoint) == 'on the line'):
                    s += 1

    if s % 2 == 0:
        return False
    else:
        return True


def init():
    plt.grid(True)  # линии вспомогательной сетки

    xs = [1, 3, 1, 5, 6, 7, 8, 9, 10, 8, 7, 6, 5, 4, 1]
    ys = [1, 5, 9, 10, 8, 9, 8, 11, 6, 3, 4, 2, 4, 2, 1]
    points = initPoints(xs, ys)
    initialPoint = Point(random.randint(0, 12), random.randint(0, 12))
    # initialPoint = Point(11, 1) #снаружи
    # initialPoint = Point(8, 9) #снаружи между сторонами
    # initialPoint = Point(7, 7) #просто внутри
    # initialPoint = Point(2, 7) #на границе
    # initialPoint = Point(11, 8) #снаружи, пересекая вершины
    # initialPoint = Point(2, 1) #снаружи, пересекая вершину

    q = Point(getMinX(points) - 1, initialPoint.y)

    drawPolygon(points)
    drawPoint(initialPoint)
    drawLine(q, initialPoint)

    if not radialTest(initialPoint, points):
        plt.suptitle('Снаружи', fontsize=14)
    elif lineOnPolygonBound(initialPoint, points):
        plt.suptitle('На границе', fontsize=14)
    elif radialTest(initialPoint, points):
        plt.suptitle('Внутри', fontsize=14)

    plt.show()


init()


