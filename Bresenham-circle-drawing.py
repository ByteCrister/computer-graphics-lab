def CalculatePosition(h, k, r, points):
    """
    Classify points relative to the circle.
    Equation: (x - h)^2 + (y - k)^2 = r^2
    """
    inside, outside, on = [], [], []
    for x, y in points:
        value = (x - h) ** 2 + (y - k) ** 2 - r**2
        if value < 0:
            inside.append((x, y))
        elif value == 0:
            on.append((x, y))
        else:
            outside.append((x, y))
    return inside, on, outside


def BresenhamCircle(h, k, r):
    """
    Bresenham’s Circle Drawing Algorithm
    """
    x, y = 0, r
    d = 3 - 2 * r
    points = []

    while x <= y:
        points.append((x + h, y + k))
        if d < 0:
            d += 4 * x + 6
        else:
            d += 4 * (x - y) + 10
            y -= 1
        x += 1
    return points


def GenerateFullCircle(points, h, k):
    """
    Expand one-octant points into full 8-way symmetry.
    """
    circle_points = []
    for x, y in points:
        dx, dy = x - h, y - k
        circle_points.extend(
            [
                (h + dx, k + dy),
                (h - dx, k + dy),
                (h + dx, k - dy),
                (h - dx, k - dy),
                (h + dy, k + dx),
                (h - dy, k + dx),
                (h + dy, k - dx),
                (h - dy, k - dx),
            ]
        )
    return list(set(circle_points))  # remove duplicates


if __name__ == "__main__":
    h, k, r = map(int, input("Enter circle center (h k) and radius r: ").split())

    # Bresenham Algorithm
    bresenham_octant = BresenhamCircle(h, k, r)
    bresenham_circle = GenerateFullCircle(bresenham_octant, h, k)
    inside_b, on_b, outside_b = CalculatePosition(h, k, r, bresenham_circle)

    print("\n--- Bresenham Circle Algorithm ---")
    print("Points:", bresenham_circle)
    print("Inside:", inside_b)
    print("On:", on_b)
    print("Outside:", outside_b)
