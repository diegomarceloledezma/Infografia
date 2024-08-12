import math
import arcade
from bresenham import get_line

# Definición de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Figuras con Bresenham"

class BresenhamWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.pixel_size = 10

    def on_update(self, delta_time: float):
        pass

    def on_draw(self):
        arcade.start_render()
        self.draw_grid()
        self.draw_rectangulo(10, 10, 50, 30, arcade.color.AZURE_MIST)
        self.draw_triangulo_isosceles(10, 10, 20, 10, 15, 20, arcade.color.RED)
        self.draw_pentagono(20, 20, 10, arcade.color.GREEN_YELLOW)

    def draw_grid(self):
        # Líneas verticales
        for v_l in range(0, SCREEN_WIDTH, self.pixel_size):
            arcade.draw_line(
                v_l + self.pixel_size / 2, 
                0, 
                v_l + self.pixel_size / 2, 
                SCREEN_HEIGHT, 
                [50, 50, 50]
            )

        # Líneas horizontales
        for h_l in range(0, SCREEN_HEIGHT, self.pixel_size):
            arcade.draw_line(
                0, 
                h_l + self.pixel_size / 2, 
                SCREEN_WIDTH, 
                h_l + self.pixel_size / 2, 
                [50, 50, 50]
            )

    def draw_line_points(self, points, color):
        for p in points:
            arcade.draw_point(p[0] * self.pixel_size, p[1] * self.pixel_size, color, self.pixel_size)

    def draw_rectangulo(self, x0, y0, x1, y1, color):
        points = get_line(x0, y0, x0, y1)  # Lado izquierdo
        self.draw_line_points(points, color)
    
        points = get_line(x0, y0, x1, y0)  # Lado inferior
        self.draw_line_points(points, color)
    
        points = get_line(x1, y0, x1, y1)  # Lado derecho
        self.draw_line_points(points, color)
    
        points = get_line(x0, y1, x1, y1)  # Lado superior
        self.draw_line_points(points, color)

    def draw_triangulo_isosceles(self, x0, y0, x1, y1, x2, y2, color):
        # Dibuja los tres lados del triángulo isósceles
        points = get_line(x0, y0, x1, y1)  # Lado entre el primer y segundo vértice
        self.draw_line_points(points, color)
    
        points = get_line(x1, y1, x2, y2)  # Lado entre el segundo y tercer vértice
        self.draw_line_points(points, color)
    
        points = get_line(x2, y2, x0, y0)  # Lado entre el tercer y primer vértice
        self.draw_line_points(points, color)

    def draw_pentagono(self, xc, yc, r, color):
        # Calcular los vértices del pentágono
        points = []
        for i in range(5):
            angle = 2 * math.pi * i / 5
            x = round(xc + r * math.cos(angle))  # Redondear a entero
            y = round(yc + r * math.sin(angle))  # Redondear a entero
            points.append((x, y))
        
        # Dibujar los bordes del pentágono
        for i in range(5):
            x0, y0 = points[i]
            x1, y1 = points[(i + 1) % 5]
            line_points = get_line(x0, y0, x1, y1)
            self.draw_line_points(line_points, color)

if __name__ == "__main__":
    app = BresenhamWindow()
    arcade.run()
