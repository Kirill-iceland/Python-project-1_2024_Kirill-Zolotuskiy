import pygame
from SpanningTree import SpanningTree
from DFS import DFS
from Maze import Maze
from Path import Path
from Button import Button


class Solve:
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

        self.generate_maze = Button(520, 850, 400, 80, 40)
        self.generate_maze.set_text('GENERATE')
        self.generate_maze.set_text_color((255, 255, 255))
        self.generate_maze.set_color((150, 150, 150))

        self.clear_path = Button(80, 850, 400, 80, 40)
        self.clear_path.set_text('CLEAR')
        self.clear_path.set_text_color((255, 255, 255))
        self.clear_path.set_color((150, 150, 150))

        self.solution = Path(self.maze)
        self.solution.append(0, 0)

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

            self.solution.draw(screen, 150, 120, 700, 700)
            self.solution.draw_last(screen, 150, 120, 700, 700)

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
                        self.maze = DFS.generate(self.width, self.height)
                    else:
                        self.maze = SpanningTree.generate(
                            self.width, self.height)
                    self.solution = Path(self.maze)
                    self.solution.append(0, 0)

                if self.clear_path.draw(screen):
                    self.solution = Path(self.maze)
                    self.solution.append(0, 0)

                if self.up_width_button.draw(screen):
                    self.width += 1
                    self.maze = Maze(self.width, self.height, 0b0000)
                    self.solution = Path(self.maze)
                    self.solution.append(0, 0)
                    pygame.draw.rect(screen, (200, 255, 255),
                                     (150, 120, 700, 700))

                if self.down_width_button.draw(screen):
                    self.width -= 1
                    self.maze = Maze(self.width, self.height, 0b0000)
                    self.solution = Path(self.maze)
                    self.solution.append(0, 0)
                    pygame.draw.rect(screen, (200, 255, 255),
                                     (150, 120, 700, 700))

                if self.up_height_button.draw(screen):
                    self.height += 1
                    self.maze = Maze(self.width, self.height, 0b0000)
                    self.solution = Path(self.maze)
                    self.solution.append(0, 0)
                    pygame.draw.rect(screen, (200, 255, 255),
                                     (150, 120, 700, 700))

                if self.down_height_button.draw(screen):
                    self.height -= 1
                    self.maze = Maze(self.width, self.height, 0b0000)
                    self.solution = Path(self.maze)
                    self.solution.append(0, 0)
                    pygame.draw.rect(screen, (200, 255, 255),
                                     (150, 120, 700, 700))

                if event.type == pygame.KEYDOWN:
                    (cell_x, cell_y) = self.solution.path[-1]
                    if (event.key == pygame.K_LEFT and not
                        self.maze.grid[cell_x][cell_y].top_wall):
                        if (len(self.solution.path) > 1 and
                            self.solution.path[-2] == (cell_x - 1, cell_y)):
                            self.solution.path.pop()
                        else:
                            self.solution.append(cell_x - 1, cell_y)

                    if (event.key == pygame.K_RIGHT and not
                        self.maze.grid[cell_x][cell_y].bottom_wall):
                        if (len(self.solution.path) > 1 and
                            self.solution.path[-2] == (cell_x + 1, cell_y)):
                            self.solution.path.pop()
                        else:
                            self.solution.append(cell_x + 1, cell_y)

                    if (event.key == pygame.K_UP and not
                        self.maze.grid[cell_x][cell_y].left_wall):
                        if (len(self.solution.path) > 1 and
                            self.solution.path[-2] == (cell_x, cell_y - 1)):
                            self.solution.path.pop()
                        else:
                            self.solution.append(cell_x, cell_y - 1)

                    if (event.key == pygame.K_DOWN and not
                        self.maze.grid[cell_x][cell_y].right_wall):
                        if (len(self.solution.path) > 1 and
                            self.solution.path[-2] == (cell_x, cell_y + 1)):
                            self.solution.path.pop()
                        else:
                            self.solution.append(cell_x, cell_y + 1)
                    
                    (cell_x, cell_y) = self.solution.path[-1]
                    if (cell_y < 0 or cell_y >= self.width or
                        cell_x < 0 or cell_x >= self.height):
                        self.solution.path.pop()

                if event.type == pygame.QUIT:
                    running = False
                    keep_open = False
            pygame.display.flip()
        return keep_open
