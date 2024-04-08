import pygame
import sys
sys.path.append('src/algorithms')
sys.path.append('src/maze')
sys.path.append('src/windows')
from SpanningTree import SpanningTree
from DFS import DFS
from BFS import BFS
from AStar import AStar
from Button import Button
from Generate import Generate
from Solve import Solve

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode([1000, 1000])
icon = pygame.image.load('src/img/icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('MazeCreator')
# pygame.draw.rect(screen, (250, 100, 100), (100, 10, 100, 10))
# maze = DFS.generate(20, 20)
# maze.draw(screen, 20, 20, 960, 960)
# path = AStar.solve(maze)
# path = Path(maze)
# path.append(0, 0)
# path.append(0, 1)
# path.append(0, 2)
# pygame.display.flip()
# path.draw(screen, 20, 20, 960, 960)
# pygame.display.flip()
generate = Button(100, 550, 800, 200, 50)
generate.set_text('GENERATE')
generate.set_text_color((255, 255, 255))
generate.set_color((150, 150, 150))

solve = Button(100, 250, 800, 200, 50)
solve.set_text('SOLVE')
solve.set_text_color((255, 255, 255))
solve.set_color((150, 150, 150))

generate_window = Generate()
solve_window = Solve()

running = True
while running:
    for event in pygame.event.get():
        if generate.draw(screen):
            running = generate_window.open(screen)
            screen.fill((0, 0, 0))
        if solve.draw(screen):
            running = solve_window.open(screen)
            screen.fill((0, 0, 0))
        if solve.draw(screen):
            running = False
        if event.type == pygame.QUIT:
            running = False
    # maze.draw(screen, 20, 20, 960, 960)
    pygame.display.flip()
pygame.quit()