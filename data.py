import pygame
from settings import WINDOW_SIZE, WIN, GRAY,BLUE
import math
import random
from pygame.locals import Color


class Particle(object):

    def __init__(self, x, y, radius, color, surface):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = Color(int(color[0]), int(color[1]), int(color[2]), 255)
        self.surface = surface

        self.rect = pygame.Rect(self.x, self.y, self.radius, self.radius)

        self.decay = random.randint(1, 4)

        self.gravity = 2
        self.speed = self.radius * .2
        self.direction = pygame.math.Vector2(0, 0)
        self.acceleration = pygame.math.Vector2(random.randint(0, 42) / 6 - 3.5, random.randint(0, 42) / 6 - 3.5)

    def update(self):
        x = self.x
        y = self.y
        self.x += self.acceleration.x
        self.y += self.acceleration.y + self.gravity

        if self.x + self.radius < 0 or self.x+self.radius > WINDOW_SIZE[0]:
            self.acceleration = pygame.math.Vector2(random.randint(0, 42) / 6 - 3.5, random.randint(0, 42) / 6 - 3.5)
            self.x += self.acceleration.x
        if self.y+self.radius < 0 or self.y+self.radius > WINDOW_SIZE[1]:
            self.acceleration = pygame.math.Vector2(random.randint(0, 42) / 6 - 3.5, random.randint(0, 42) / 6 - 3.5)
            self.y += self.acceleration.y * self.gravity

        self.rect = pygame.Rect(self.x, self.y, self.radius, self.radius)
        if self.color.a > self.decay:
            self.color.a -= self.decay
        elif self.color.a - self.decay <= 0:
            self.color.a = 0
        else:
            print(self.color.a)

    def draw(self):
        pygame.draw.circle(self.surface, self.color, [int(self.x), int(self.y)], self.radius)

    def sim(self):
        rand = random.uniform(0, 1)
        angle = 360*rand
        self.acceleration.x = self.speed * math.sin(angle)
        self.acceleration.y = self.speed * math.cos(angle) + self.gravity

