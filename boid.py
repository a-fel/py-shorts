X_MIN = 0
X_MAX = 500
Y_MIN = 0
Y_MAX = 500
# from random import randint
import random
from enum import Enum

class Vector():
    def __init__(self, x = random.randint(X_MIN, X_MAX), y = random.randint(X_MIN, X_MAX)):
        assert x in range(X_MIN, X_MAX+1)
        assert y in range(Y_MIN, Y_MAX+1)
        self.x = x
        self.y = y


class Direction(Enum):
    up = 1
    down = 2
    right = 3
    left = 4

class Boid():
    def __init__(self):
        self.position = Vector(random.randint(X_MIN, X_MAX), random.randint(Y_MIN, Y_MAX))
        # self.position = Vector(250, 250)
        self.velocity = Vector(random.randint(X_MIN, X_MAX // 100), random.randint(Y_MIN, Y_MAX // 100))
        self.acceleration = Vector(0, 0)

    def __str__(self):
        return f"Position = {self.position.x}, {self.position.y}\nVelocity = {self.velocity.x}, {self.velocity.y}\nAcceleration = {self.acceleration.x}, {self.acceleration.y}"

    def move(self):
        self.position.x += self.velocity.x + 0.5 * self.acceleration.x # x(t) = x_0 + v_0 * t + 0.5 * a * t ^ 2, when t, the time unit, is 1
        self.position.y += self.velocity.y + 0.5 * self.acceleration.y  # x(t) = x_0 + v_0 * t + 0.5 * a * t ^ 2, when t, the time unit, is 1

    def collision(self):

        if self.position.x >= X_MAX or self.position.x <= X_MIN:
            self.velocity.x *= -1
        if self.position.y >= Y_MAX or self.position.y <= Y_MIN:
            self.velocity.y *= -1


    def change_direction(self):
        change = random.choice(["Left", "Right", "Up", "Down", "Up Left", "Up Right", "Down Left", "Down Right"])
        print(f"Changing direction: {change}")
        if change == "Left":
            self.velocity.x = (self.velocity.x * -1) if self.velocity.x < 0 else self.velocity.x
        elif change == "Right":
            self.velocity.x = (self.velocity.x * -1) if self.velocity.x > 0 else self.velocity.x
        elif change == "Up":
            self.velocity.y = (self.velocity.y * -1) if self.velocity.y > 0 else self.velocity.y
        elif change == "Down":
            self.velocity.y = (self.velocity.y * -1) if self.velocity.y < 0 else self.velocity.y
        elif change == "Up Left":
            self.velocity.y = (self.velocity.y * -1) if self.velocity.y > 0 else self.velocity.y
            self.velocity.x = (self.velocity.x * -1) if self.velocity.x < 0 else self.velocity.x
        elif change == "Up Right":
            self.velocity.y = (self.velocity.y * -1) if self.velocity.y > 0 else self.velocity.y
            self.velocity.x = (self.velocity.x * -1) if self.velocity.x > 0 else self.velocity.x
        elif change == "Down Left":
            self.velocity.y = (self.velocity.y * -1) if self.velocity.y < 0 else self.velocity.y
            self.velocity.x = (self.velocity.x * -1) if self.velocity.x < 0 else self.velocity.x
        elif change == "Down Right":
            self.velocity.y = (self.velocity.y * -1) if self.velocity.y < 0 else self.velocity.y
            self.velocity.x = (self.velocity.x * -1) if self.velocity.x > 0 else self.velocity.x