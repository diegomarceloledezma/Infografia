def get_circle(xc, yc, r):
    points = []
    x = 0
    y = r
    Pk = 3 - 2 * r
    
    def add_circle_points(xc, yc, x, y):
        # Agrega los puntos en todos los octantes
        points.append((xc + x, yc + y))
        points.append((xc - x, yc + y))
        points.append((xc + x, yc - y))
        points.append((xc - x, yc - y))
        points.append((xc + y, yc + x))
        points.append((xc - y, yc + x))
        points.append((xc + y, yc - x))
        points.append((xc - y, yc - x))
    
    add_circle_points(xc, yc, x, y)
    
    while x <= y:
        x += 1
        if Pk < 0:
            Pk += (4 * x) + 6
        else:
            Pk += 4 * (x - y) + 10
            y -= 1
        add_circle_points(xc, yc, x, y)
    
    return points
