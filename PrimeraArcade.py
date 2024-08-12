import arcade

# Dimensiones de la ventana
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
WINDOW_TITLE = "hola arcade"

class HelloWindow(arcade.Window):
    def __init__(self, width, height, title):
        # Inicializar la clase base
        super().__init__(width, height, title)
        # Fondo:
        arcade.set_background_color(arcade.color.AMETHYST)

    def on_draw(self):
        arcade.start_render()

# Crear la ventana con los parámetros correctos
window = HelloWindow(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

# Ejecutar el ciclo principal del juego
arcade.run()
