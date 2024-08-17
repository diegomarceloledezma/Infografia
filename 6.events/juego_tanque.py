import arcade
import math
from game_object import Polygon2D

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Tank Game"

class Tank(Polygon2D):
    def __init__(self, position, color):
        body = [
            (position[0] - 20, position[1] - 20),
            (position[0] - 20, position[1] + 20),
            (position[0] + 20, position[1] + 20),
            (position[0] + 20, position[1] - 20),
        ]
        super().__init__(body, color)
        self.position = position
        self.angle = 0  # Angle in radians

    def draw(self):
        # Draw the body of the tank (square)
        super().draw()

        # Draw the turret (circle)
        center_x, center_y = self.get_center()
        arcade.draw_circle_filled(center_x, center_y, 15, self.color)

        # Draw the cannon (rectangle)
        cannon_length = 40
        cannon_width = 10
        end_x = center_x + math.cos(self.angle) * cannon_length
        end_y = center_y + math.sin(self.angle) * cannon_length
        arcade.draw_line(
            center_x, center_y, end_x, end_y, self.color, cannon_width
        )

    def move(self, speed):
        dx = math.cos(self.angle) * speed
        dy = math.sin(self.angle) * speed
        self.translate(dx, dy)
        self.position[0] += dx
        self.position[1] += dy

    def rotate(self, theta):
        super().rotate(theta)
        self.angle += theta

    def shoot(self):
        center_x, center_y = self.get_center()
        bullet_x = center_x + math.cos(self.angle) * 40  # Position the bullet at the end of the cannon
        bullet_y = center_y + math.sin(self.angle) * 40
        return Bullet(bullet_x, bullet_y, self.angle)

class Bullet(Polygon2D):
    def __init__(self, x, y, angle):
        self.position = [x, y]
        self.angle = angle
        self.speed = 10
        vertices = [
            (x - 5, y - 5),
            (x - 5, y + 5),
            (x + 5, y + 5),
            (x + 5, y - 5),
        ]
        super().__init__(vertices, arcade.color.RED)

    def update(self):
        dx = math.cos(self.angle) * self.speed
        dy = math.sin(self.angle) * self.speed
        self.translate(dx, dy)
        self.position[0] += dx
        self.position[1] += dy

    def draw(self):
        arcade.draw_circle_filled(self.position[0], self.position[1], 5, arcade.color.RED)

class App(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.tank = Tank([SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2], arcade.color.GREEN)
        self.bullets = []
        self.keys = set()

    def on_key_press(self, symbol: int, modifiers: int):
        self.keys.add(symbol)
        if symbol == arcade.key.SPACE:
            self.bullets.append(self.tank.shoot())

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol in self.keys:
            self.keys.remove(symbol)

    def on_update(self, delta_time: float):
        if arcade.key.UP in self.keys:
            self.tank.move(5)
        if arcade.key.DOWN in self.keys:
            self.tank.move(-5)
        if arcade.key.LEFT in self.keys:
            self.tank.rotate(math.radians(3))
        if arcade.key.RIGHT in self.keys:
            self.tank.rotate(math.radians(-3))

        for bullet in self.bullets:
            bullet.update()

    def on_draw(self):
        arcade.start_render()
        self.tank.draw()
        for bullet in self.bullets:
            bullet.draw()

if __name__ == "__main__":
    app = App()
    arcade.run()
