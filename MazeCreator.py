import pygame
import sys
sys.path.append('src/algorithms')
sys.path.append('src/maze')
from SpanningTree import SpanningTree

pygame.init()

screen = pygame.display.set_mode([1000, 1000])
icon = pygame.image.load('src/img/icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('MazeCreator')
# pygame.draw.rect(screen, (250, 100, 100), (100, 10, 100, 10))
maze = SpanningTree.generate(100, 100)
maze.draw(screen)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()

print(1)