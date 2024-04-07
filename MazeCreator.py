import pygame
import sys
sys.path.append('src/algorithms')
sys.path.append('src/maze')
from SpanningTree import SpanningTree

pygame.init()

screen = pygame.display.set_mode([500, 500])
pygame.draw.rect(screen, (250, 100, 100), (100, 10, 100, 10))
maze = SpanningTree.generate(5, 5)
maze.draw(screen)
pygame.display.flip()
while (True):
    1 + 1

print(1)