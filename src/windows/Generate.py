import pygame
from SpanningTree import SpanningTree
from DFS import DFS
from AStar import AStar
from BFS import BFS
from Maze import Maze
from Path import Path
from Button import Button

class Generate:

    def __init__(self):
        self.width = 20
        self.hight = 20
        self.maze = Maze(self.width, self.hight, 0b0000)

        self.back = Button(50, 50, 100, 50, 30)
        self.back.set_text('BACK')
        self.back.set_text_color((255, 255, 255))
        self.back.set_color((150, 150, 150))

        self.generator_type = 'DFS'

        self.generator_button = Button(650, 50, 300, 50, 30)
        self.generator_button.set_text(self.generator_type)
        self.generator_button.set_text_color((255, 255, 255))
        self.generator_button.set_color((150, 150, 150))

        self.generate_maze = Button(520, 850, 400, 80, 40)
        self.generate_maze.set_text('GENERATE')
        self.generate_maze.set_text_color((255, 255, 255))
        self.generate_maze.set_color((150, 150, 150))

        self.solve_maze = Button(80, 850, 400, 80, 40)
        self.solve_maze.set_text('SOLVE')
        self.solve_maze.set_text_color((255, 255, 255))
        self.solve_maze.set_color((150, 150, 150))

        self.solution: Path
        self.solve = False

    def open(self, screen: pygame.Surface) -> bool:
        screen.fill((200, 255, 255))
        running = True
        keep_open = True
        while running:
            self.maze.draw(screen, 150, 120, 700, 700)
            if self.solve:
                self.solution.draw(screen, 150, 120, 700, 700)

            for event in pygame.event.get():
                if self.back.draw(screen):
                    running = False

                if self.generator_button.draw(screen):
                    if self.generator_type == 'DFS':
                        self.generator_type = 'SPANNING TREE'
                    else:
                        self.generator_type = 'DFS'
                    self.generator_button.set_text(self.generator_type)

                if self.generate_maze.draw(screen):
                    if self.generator_type == 'DFS':
                        self.maze = DFS.generate(self.width, self.hight)
                    else:
                        self.maze = SpanningTree.generate(self.width, self.hight)
                    pass

                if self.solve_maze.draw(screen):
                    if self.solve:
                        self.solve = False
                        self.solve_maze.set_text('SOLVE')
                    else:
                        self.solution = AStar.solve(self.maze)
                        self.solve = True
                        self.solve_maze.set_text('UNSOLVE')

                if event.type == pygame.QUIT:
                    running = False
                    keep_open = False
            pygame.display.flip()
        return keep_open
