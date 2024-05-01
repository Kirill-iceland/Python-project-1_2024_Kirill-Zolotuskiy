import os

import pygame

from src.windows.button import Button
from src.windows.generate import Generate
from src.windows.solve import Solve


class MazeCreator:
    def start():
        pygame.init()
        pygame.font.init()

        screen = pygame.display.set_mode([1000, 1000])
        icon = pygame.image.load(os.path.join('src', 'img', 'icon.png'))
        pygame.display.set_icon(icon)
        pygame.display.set_caption('MazeCreator')
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

            pygame.display.flip()
        pygame.quit()

if __name__ == '__main__':
    MazeCreator.start()
