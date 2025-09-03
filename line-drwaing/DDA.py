import matplotlib.pyplot as plt


def DDA(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    steps = int(max(abs(dx), abs(dy)))

    XInc = dx / steps
    YInc = dy / steps

    x = x1
    y = y1

    points = []

    for _ in range(steps):
        points.append((round(x), round(y)))
        x += XInc
        y += YInc

    return points


if __name__ == "__main__":
    x1, y1, x2, y2 = map(int, input(f"Enter x1, y1, x2, y2: ").split())
    pixels = DDA(x1, y1, x2, y2)
    
    xs, ys = zip(*pixels)
    plt.figure(figsize=(5, 5))
    plt.scatter(xs, ys, c="red", s=50)
    plt.plot(xs, ys, c="blue", linewidth=1)
    plt.title("DDA Line")
    plt.grid(True)
    plt.axis("equal")
    plt.show()
