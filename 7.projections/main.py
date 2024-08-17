import arcade
import numpy as np
import random
import math
from game_object import Object3D

# Definición de constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Proyección 3D con Mouse"


def get_random_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )


class App(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.pyramid = Object3D(
            [
                (1, 1, 0),    # Vértice 0 - superior derecho de la base
                (1, -1, 0),   # Vértice 1 - inferior derecho de la base
                (-1, -1, 0),  # Vértice 2 - inferior izquierdo de la base
                (-1, 1, 0),   # Vértice 3 - superior izquierdo de la base
                (0, 0, 1),    # Vértice 4 - vértice superior de la pirámide (punta)
            ],
            [
                (0, 1),  # Lado derecho de la base
                (1, 2),  # Lado inferior de la base
                (2, 3),  # Lado izquierdo de la base
                (3, 0),  # Lado superior de la base
                (0, 4),  # Conexión del vértice superior derecho al vértice superior de la pirámide
                (1, 4),  # Conexión del vértice inferior derecho al vértice superior de la pirámide
                (2, 4),  # Conexión del vértice inferior izquierdo al vértice superior de la pirámide
                (3, 4)   # Conexión del vértice superior izquierdo al vértice superior de la pirámide
            ],
            arcade.color.YELLOW
        )
        self.pyramid.translate(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 0)
        self.pyramid.scale(100, 100, 100)

    def on_mouse_motion(self, x, y, dx, dy):
        # Obtener la posición del vértice superior de la pirámide (punta)
        pyramid_tip = np.array(self.pyramid.vertices[4])

        # Calcular el vector dirección desde la punta de la pirámide hacia el cursor
        direction = np.array([x - pyramid_tip[0], y - pyramid_tip[1]])

        # Calcular la longitud del vector dirección
        length = np.linalg.norm(direction)

        if length > 0:
            # Normalizar el vector dirección
            direction = direction / length

            # Calcular el ángulo en radianes que debe rotar la pirámide
            angle_y = math.atan2(direction[0], 1)  # Rotación alrededor del eje Y
            angle_x = -math.atan2(direction[1], 1)  # Rotación alrededor del eje X

            # Rotar la pirámide suavemente hacia el cursor
            self.pyramid.rotate(angle_x * 0.05, "x")
            self.pyramid.rotate(angle_y * 0.05, "y")

    def on_draw(self):
        arcade.start_render()
        self.pyramid.draw()


if __name__ == "__main__":
    app = App()
    arcade.run()
