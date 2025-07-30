def DDA(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))

    XInc = round(dx / steps)
    YInc = round(dy / steps)

    x = x1
    y = x2

    points = []

    for _ in range(steps):
        points.append((x, y))
        x += XInc
        y += YInc

    return points

x1, y1, x2, y2 = map(int, input(f"Enter x1, y1, x2, y2: ").split(" "))
print(DDA(x1, y1, x2, y2))
