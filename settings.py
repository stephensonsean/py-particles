import pygame

pygame.init()

FONT = pygame.font.SysFont('Times New Roman', 30)
TITLE = 'Towers of Hanoi'
CLOCK = pygame.time.Clock()

# game window size
WINDOW_SIZE = (1280, 720)
WIN = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
# Window Title
pygame.display.set_caption(TITLE)

OFF_WHITE = (233, 233, 233)
GRAY = (100, 100, 100)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)