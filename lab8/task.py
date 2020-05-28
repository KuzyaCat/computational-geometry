import matplotlib.pyplot as plt


def point_of_intersection(a, b, c, d):
    delta_x = (a[0] - b[0], c[0] - d[0])
    delta_y = (a[1] - b[1], c[1] - d[1])

    def det(i, j):
        return i[0] * j[1] - i[1] * j[0]

    div = det(delta_x, delta_y)
    d = (det(a, b), det(c, d))
    x = det(d, delta_x) / div
    y = det(d, delta_y) / div
    return x, y


def slanting_product(a, b, c, d):
    return (b[0] - a[0]) * (d[1] - c[1]) - (b[1] - a[1]) * (d[0] - c[0])


def scalar_product(a_start, a_end, b_start, b_end):
    return (a_end[0] - a_start[0]) * (b_end[0] - b_start[0]) + (a_end[1] - a_start[1]) * (b_end[1] - b_start[1])


def det(a, b, c, d):
    return a * d - b * c


def point_position(p0: tuple, p1: tuple, p2: tuple) -> str:
    d = det(p2[0] - p1[0], p2[1] - p1[1], p0[0] - p1[0], p0[1] - p1[1])
    if d > 0:
        return 'left'
    elif d < 0:
        return 'right'
    else:
        return 'on the line'


def is_directed(a_start, a_end, b_start, b_end):
    if slanting_product(b_start, b_end, b_start, a_end) > 0 and slanting_product(b_start, b_end, a_start, a_end) < 0:
        return True
    if slanting_product(b_start, b_end, b_start, a_end) < 0 and slanting_product(b_start, b_end, a_start, a_end) > 0:
        return True
    return scalar_product(a_end, a_start, a_end, b_end) < 0


def is_outer(a_start, a_end, b_end):
    return point_position(a_start, a_end, b_end) == 'right'


def init_lines(left_polygon: list, right_polygon: list):
    for i, point_q in enumerate(right_polygon):
        if is_outer(left_polygon[0], left_polygon[1], point_q) or \
                is_outer(right_polygon[i], right_polygon[(i + 1) % len(right_polygon)], left_polygon[1]):
            return 0, i


def are_intersect(p1: tuple, p2: tuple, p3: tuple, p4: tuple) -> bool:
    d1 = det(p4[0] - p3[0], p4[1] - p3[1], p1[0] - p3[0], p1[1] - p3[1])
    d2 = det(p4[0] - p3[0], p4[1] - p3[1], p2[0] - p3[0], p2[1] - p3[1])
    d3 = det(p2[0] - p1[0], p2[1] - p1[1], p3[0] - p1[0], p3[1] - p1[1])
    d4 = det(p2[0] - p1[0], p2[1] - p1[1], p4[0] - p1[0], p4[1] - p1[1])

    if d1 * d2 <= 0 and d3 * d4 <= 0:
        return True
    else:
        return False


def polygon_intersection(left_polygon: list, right_polygon: list):
    p_index, q_index = init_lines(left_polygon, right_polygon)
    res = []
    while True:
        p_to_q = is_directed(left_polygon[p_index], left_polygon[(p_index + 1) % len(left_polygon)], right_polygon[q_index],
                      right_polygon[(q_index + 1) % len(right_polygon)])
        q_to_p = is_directed(right_polygon[q_index], right_polygon[(q_index + 1) % len(right_polygon)], left_polygon[p_index],
                      left_polygon[(p_index + 1) % len(left_polygon)])

        # p to q & q to p
        if p_to_q and q_to_p:
            if is_outer(left_polygon[p_index], left_polygon[(p_index + 1) % len(left_polygon)],
                              right_polygon[(q_index + 1) % len(right_polygon)]):
                q_index += 1 if q_index + 1 < len(right_polygon) else -len(right_polygon) + 1
            else:
                p_index += 1 if p_index + 1 < len(left_polygon) else -len(left_polygon) + 1

        # p to q & q not to p
        elif p_to_q and not q_to_p:
            if not is_outer(right_polygon[q_index], right_polygon[(q_index + 1) % len(right_polygon)],
                                  left_polygon[(p_index + 1) % len(left_polygon)]):
                res.append(left_polygon[(p_index + 1) % len(left_polygon)])
            p_index += 1 if p_index + 1 < len(left_polygon) else -len(left_polygon) + 1

        # p not to q & q to p
        elif not p_to_q and q_to_p:
            if not is_outer(left_polygon[p_index], left_polygon[(p_index + 1) % len(left_polygon)],
                                  right_polygon[(q_index + 1) % len(right_polygon)]):
                res.append(right_polygon[(q_index + 1) % len(right_polygon)])
            q_index += 1 if q_index + 1 < len(right_polygon) else -len(right_polygon) + 1

        # p not to q & q not to p
        else:
            if are_intersect(left_polygon[p_index], left_polygon[(p_index + 1) % len(left_polygon)],
                                     right_polygon[q_index], right_polygon[(q_index + 1) % len(right_polygon)]):
                res.append(point_of_intersection(left_polygon[p_index], left_polygon[(p_index + 1) % len(left_polygon)],
                                                     right_polygon[q_index], right_polygon[(q_index + 1) % len(right_polygon)]))
            if is_outer(left_polygon[p_index], left_polygon[(p_index + 1) % len(left_polygon)],
                                     right_polygon[(q_index + 1) % len(right_polygon)]):
                q_index += 1 if q_index + 1 < len(right_polygon) else -len(right_polygon) + 1
            else:
                p_index += 1 if p_index + 1 < len(left_polygon) else -len(left_polygon) + 1

        if len(res) > 1:
            if res[0] == res[-1]:
                res.pop()
                break

    return res


def draw_polygon(points: list, color):
    for i in range(len(points)):
        plt.plot([points[i][0], points[(i + 1) % len(points)][0]], [points[i][1], points[(i + 1) % len(points)][1]],
                 color=color)


def draw_polygons(left_polygon: list, right_polygon: list):
    draw_polygon(left_polygon, "red")
    draw_polygon(right_polygon, "blue")


def init():
    left_polygon = [(9, 7), (-6, 5), (-10, 2), (-9, -5), (3, -10), (6, -10), (8, -5), (10, 6)]
    right_polygon = [(1, 10), (-7, 9), (-8, 4), (-7, -2), (-6, -5), (1, -2), (3, 6)]
    draw_polygons(left_polygon, right_polygon)
    draw_polygon(polygon_intersection(left_polygon, right_polygon), "green")
    plt.grid(True)
    plt.show()


init()

