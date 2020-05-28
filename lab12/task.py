from matplotlib import pyplot as plt
from celluloid import Camera


# bezier curves (recursion)


fig = plt.figure()
camera = Camera(fig)
ax = fig.gca


def init_control_points():
    return [(1, 1), (2, 20), (7, -5), (10, 5)]


def make_bezier(control_points: list, t: float, bezier_points: list):
    def choose_point(p1, p2, t):
        return p1[0] + (p2[0] - p1[0]) * t, p1[1] + (p2[1] - p1[1]) * t

    chosen_points = []

    for i in range(len(control_points) - 1):
        chosen_point = choose_point(control_points[i], control_points[i + 1], t)

        if len(control_points) <= 2:
            bezier_points.append(chosen_point)
            return

        chosen_points.append(chosen_point)

    if len(chosen_points) >= 2:
        make_bezier(chosen_points, t, bezier_points)


def bezier_curve(control_points: list):
    t_begin = 0
    t_end = 1
    t_step = 0.01

    bezier_points = []
    t = t_begin

    while t <= t_end:
        make_bezier(control_points, t, bezier_points)
        t += t_step

    return bezier_points


def draw_point(point: tuple):
     plt.scatter(point[0], point[1])


def animate(control_points: list, bezier_points: list):
    for i in range(len(bezier_points)):
        draw_segments(control_points, "green")
        draw_segments(bezier_points, "red")
        draw_point(bezier_points[i])
        camera.snap()


def draw_segments(points: list, color: str):
    for i in range(len(points) - 1):
        plt.plot([points[i][0], points[i + 1][0]], [points[i][1], points[i + 1][1]], color=color)


def init():
    control_points = init_control_points()
    bezier_points = bezier_curve(control_points)

    animate(control_points, bezier_points)
    animation = camera.animate(blit=False, interval=300)

    plt.grid(True)
    plt.show()


init()


# bezier curves (Bernstein polynomial)


# fig = plt.figure()
# camera = Camera(fig)
#
#
# def init_control_points():
#     return [(1, 1), (2, 20), (7, -5), (10, 5)]
#
#
# def print_points(points: list):
#     for i in range(len(points)):
#         print("i: ", i, ": ", points[i][0], ":", points[i][1])
#
#
# def draw_point(point: tuple):
#     plt.scatter(point[0], point[1])
#
#
# def det(a, b, c, d):
#     return a * d - b * c
#
#
# def bernstein_polynom(t: float, control_points: list):
#     n = len(control_points)
#     Bx = 0
#     By = 0
#
#     for i in range(1, n + 1):
#         #print (i)
#         coefficient = (math.factorial(n) / (math.factorial(i) * math.factorial(n - i))) * pow(1 - t, n - i) * pow(t, i)
#         Bx += coefficient * control_points[i - 1][0]
#         By += coefficient * control_points[i - 1][1]
#
#     return Bx, By
#
#
# def bezier_curve(points: list):
#     t_step = 0.01
#     t_begin = 0.01
#     t_end = 1
#     bezier_points = []
#
#     t = t_begin
#
#     while t <= t_end:
#         bezier_points.append(bernstein_polynom(t, points))
#         animate(bezier_points[len(bezier_points) - 1])
#         t += t_step
#     return bezier_points
#
#
# def draw_point(point: tuple):
#     plt.scatter(point[0], point[1])
#
#
# def draw_points(points: list):
#     for i in range(len(points)):
#         draw_point(points[i])
#
#
# def draw_bezier(points: list):
#     draw_segments(control_points, "green")
#     bezier_points = bezier_curve(points)
#     # draw_points(bezier_points)
#     draw_segments(bezier_points, "red")
#
#
# def animate(point: tuple):
#     draw_point(point)
#     camera.snap()
#
#
# def draw_segments(control_points: list, color: str):
#     for i in range(len(control_points) - 1):
#         plt.plot([control_points[i][0], control_points[i + 1][0]], [control_points[i][1], control_points[i + 1][1]], color=color)
#
#
# if __name__ == "__main__":
#     control_points = init_control_points()
#     print_points(control_points)
#     draw_bezier(control_points)
#     plt.grid(True)
#     plt.show()
