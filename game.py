import sys
import pygame
from pygame.locals import *
import random
import colour

from data import Particle
from settings import *

pinks = ['#fa7fe5', '#ffd4f8']
blues = ['#1976a8', '#a6173d']


class ParticleTest(object):

    def __init__(self):
        self.game_loop = True
        self.particles = []
        self.particle_layer = pygame.Surface((WINDOW_SIZE[0], WINDOW_SIZE[1]), pygame.SRCALPHA)

    def update(self):
        to_delete = []
        for p in self.particles:
            p.update()
            if p.color.a == 0:
                to_delete.append(p)

        for x in to_delete:
            self.particles.remove(x)

    def draw(self):
        WIN.fill([56, 25, 33])
        self.particle_layer.fill([56, 25, 33])

        for p in self.particles:
            p.draw()

        WIN.blit(self.particle_layer, (0, 0))


        pygame.display.update()

    def loop(self):
        while self.game_loop:
            self.event()

            self.update()

            self.draw()

            CLOCK.tick(60)

    def event(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                color = colour.Color(blues[0])
                colors = list(color.range_to(colour.Color(blues[1]), 15))
                for i in range(15):
                    c = colors[i].get_rgb()
                    self.particles.append(
                        Particle(x, y, random.randint(3, 20), [c[0]*255, c[1]*255, c[2]*255], self.particle_layer))

            if event.type == pygame.KEYDOWN:
                pass


def text_objects(text, font):
    test_surface = font.render(text, True, BLACK)
    return test_surface, test_surface.get_rect()


def main():
    game = ParticleTest()
    game.loop()


if __name__ == '__main__':
    main()
