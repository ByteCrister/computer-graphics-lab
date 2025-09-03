def Bresenhams(x1, y1, x2, y2):
    x = x1
    y = y1

    dX = x2 - x1
    dY = y2 - y1

    m = dY / dX

    if m >= 0:
        print("Slope is positive")
    elif m < 0:
        print("Slope is negative")
    elif m == 0:
        print("Slope is vertical")
    else:
        print("Slope is horizontal")

    p = 2 * dY - dX

    points = []
    steps = 0

    while x <= x2:
        points.append((x, y))
        prev = p
        x += 1
        if p < 0:
            p += 2 * dY
        else:
            p += 2 * dY - 2 * dX
            y += 1
        steps += 1
        print("(", prev, "->", p, ")")

    print("steps:", steps)
    return points


if __name__ == "__main__":
    x1, y1, x2, y2 = map(int, input("Enter x1, y1, x2, y2: ").split())

    points = Bresenhams(x1, y1, x2, y2)
    print("points are: ", *points)
