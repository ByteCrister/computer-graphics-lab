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


def MidPointCircle(h, k, r):
    """
    Midpoint Circle Drawing Algorithm
    """
    x, y = 0, r
    d = 1 - r
    points = []

    while x <= y:
        points.append((x + h, y + k))
        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
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

    # Midpoint Algorithm
    midpoint_octant = MidPointCircle(h, k, r)
    midpoint_circle = GenerateFullCircle(midpoint_octant, h, k)
    inside_m, on_m, outside_m = CalculatePosition(h, k, r, midpoint_circle)

    print("\n--- Midpoint Circle Algorithm ---")
    print("Points:", midpoint_circle)
    print("Inside:", inside_m)
    print("On:", on_m)
    print("Outside:", outside_m)
