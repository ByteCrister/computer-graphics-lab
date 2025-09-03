def fill_points(x, y, points):
    points.append((x, y))
    points.append((-x, y))
    points.append((x, -y))
    points.append((-x, -y))


def draw_ellipse(a, b):
    x = 0
    y = b

    dx = 2 * (b**2) * x
    dy = 2 * (a**2) * y

    p = (b**2) - ((a**2) * b) + ((a**2) / 4)

    points = []

    while dx < dy:
        x += 1
        dx += 2 * (b**2)
        if p < 0:
            p += 2 * (b**2) * x + b**2
        else:
            y -= 1
            p += 2 * (b**2) * x + b**2 - 2 * (a**2) * y
        fill_points(x, y, points)

    p = ((b**2) * (x + 0.5) ** 2) + ((a**2) * (y - 1) ** 2) - ((a**2) * (b**2))

    while y >= 0:
        y -= 1
        if p > 0:
            p -= 2 * (a**2) * y + (a**2)
        else:
            x += 1
            p += (2 * (b**2) * x) - (2 * (a**2) * y) + (a**2)
        fill_points(x, y, points)

    return points


def show_axis(a, b):
    if a > b:
        print("Largest:", a, " Smallest:", b)
    else:
        print("Largest:", b, " Smallest:", a)


if __name__ == "__main__":

    a, b = map(int, input("Input a & b: ").split())
    ellipse_points = draw_ellipse(a, b)

    show_axis(a, b)
    print("Ellipse: ", *ellipse_points)
