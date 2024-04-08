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
        self.height = 20
        self.maze = Maze(self.width, self.height, 0b0000)

        self.my_font = pygame.font.SysFont('Consolas', 30)
        self.my_font.bold = True

        self.rect_width = pygame.rect.Rect(25, 250, 50, 50)
        self.rect_height = pygame.rect.Rect(75, 250, 50, 50)

        self.back = Button(25, 30, 100, 50, 30)
        self.back.set_text('BACK')
        self.back.set_text_color((255, 255, 255))
        self.back.set_color((150, 150, 150))

        self.generator_type = 'DFS'

        self.generator_button = Button(520, 50, 300, 50, 30)
        self.generator_button.set_text(self.generator_type)
        self.generator_button.set_text_color((255, 255, 255))
        self.generator_button.set_color((150, 150, 150))

        self.solver_type = 'BFS'

        self.solver_button = Button(180, 50, 300, 50, 30)
        self.solver_button.set_text(self.solver_type)
        self.solver_button.set_text_color((255, 255, 255))
        self.solver_button.set_color((150, 150, 150))

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

        self.up_width_button = Button(25, 200, 50, 50, 30)
        self.up_width_button.set_text('\u25b2')
        self.up_width_button.set_text_color((255, 255, 255))
        self.up_width_button.set_color((150, 150, 150))

        self.down_width_button = Button(25, 300, 50, 50, 30)
        self.down_width_button.set_text('\u25bc')
        self.down_width_button.set_text_color((255, 255, 255))
        self.down_width_button.set_color((150, 150, 150))

        self.up_height_button = Button(75, 200, 50, 50, 30)
        self.up_height_button.set_text('\u25b2')
        self.up_height_button.set_text_color((255, 255, 255))
        self.up_height_button.set_color((150, 150, 150))

        self.down_height_button = Button(75, 300, 50, 50, 30)
        self.down_height_button.set_text('\u25bc')
        self.down_height_button.set_text_color((255, 255, 255))
        self.down_height_button.set_color((150, 150, 150))

    def open(self, screen: pygame.Surface) -> bool:
        screen.fill((200, 255, 255))
        running = True
        keep_open = True
        while running:
            self.maze.draw(screen, 150, 120, 700, 700)
            pygame.draw.rect(screen, (150, 150, 150), self.rect_width)
            text = self.my_font.render(str(self.width), True, (255, 255, 255))
            screen.blit(text, (self.rect_width.center[0] - (text.get_size()[
                        0] / 2), self.rect_width.center[1] - (text.get_size()[1] / 2)))
            pygame.draw.rect(screen, (150, 150, 150), self.rect_height)
            text = self.my_font.render(str(self.height), True, (255, 255, 255))
            screen.blit(text, (self.rect_height.center[0] - (text.get_size()[
                        0] / 2), self.rect_height.center[1] - (text.get_size()[1] / 2)))
            
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

                if self.solver_button.draw(screen):
                    if self.solver_type == 'BFS':
                        self.solver_type = 'A*'
                    else:
                        self.solver_type = 'BFS'
                    self.solver_button.set_text(self.solver_type)

                if self.generate_maze.draw(screen):
                    if self.generator_type == 'DFS':
                        self.maze = DFS.generate(self.width, self.height)
                    else:
                        self.maze = SpanningTree.generate(self.width, self.height)

                if self.solve_maze.draw(screen):
                    if self.solve:
                        self.solve = False
                        self.solve_maze.set_text('SOLVE')
                    else:
                        if self.solver_type == 'BFS':
                            self.solution = BFS.solve(self.maze)
                        else:
                            self.solution = AStar.solve(self.maze)
                        self.solve = True
                        self.solve_maze.set_text('UNSOLVE')

                if self.up_width_button.draw(screen):
                    self.width += 1
                    self.maze = Maze(self.width, self.height, 0b0000)
                    self.solve = False
                    self.solve_maze.set_text('SOLVE')
                    pygame.draw.rect(screen, (200, 255, 255), (150, 120, 700, 700))

                if self.down_width_button.draw(screen):
                    self.width -= 1
                    self.maze = Maze(self.width, self.height, 0b0000)
                    self.solve = False
                    self.solve_maze.set_text('SOLVE')
                    pygame.draw.rect(screen, (200, 255, 255), (150, 120, 700, 700))

                if self.up_height_button.draw(screen):
                    self.height += 1
                    self.maze = Maze(self.width, self.height, 0b0000)
                    self.solve = False
                    self.solve_maze.set_text('SOLVE')
                    pygame.draw.rect(screen, (200, 255, 255), (150, 120, 700, 700))

                if self.down_height_button.draw(screen):
                    self.height -= 1
                    self.maze = Maze(self.width, self.height, 0b0000)
                    self.solve = False
                    self.solve_maze.set_text('SOLVE')
                    pygame.draw.rect(screen, (200, 255, 255), (150, 120, 700, 700))

                if event.type == pygame.QUIT:
                    running = False
                    keep_open = False
            pygame.display.flip()
        return keep_open
