def get_line(x0, y0, x1, y1):
    points = []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while True:
        points.append((x0, y0))
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

    return points


if __name__ == "__main__":
    x0 = 3
    y0 = 2
    x1 = 15
    y1 = 11
    points = get_line(x0, y0, x1, y1)
    print(points)


def get_circle(xc, yc, r):
    points = []
    x = 0
    y = r
    Pk = 3 - 2 * r
    points += get_symetry_points(xc, yc, x, y)
    while x <= y:
        x += 1
        if Pk < 0:
            Pk += (4 * x) + 6
        else:
            Pk += 4 * (x - y) + 10
            y -= 1
        points += get_symetry_points(xc, yc, x, y)
    return points


def get_symetry_points(xc, yc, x, y):
    return [
        (xc+x, yc+y),
        (xc-x, yc+y),
        (xc+x, yc-y),
        (xc-x, yc-y),
        (xc+y, yc+x),
        (xc-y, yc+x),
        (xc+y, yc-x),
        (xc-y, yc-x),
    ]