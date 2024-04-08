import pygame
from Maze import Maze


class Path:
    def __init__(self, maze: Maze):
        self.path = []
        self.maze = maze

    def append(self, cell_x: int, cell_y: int):
        self.path.append((cell_x, cell_y))

    def draw_last(self, screen: pygame.Surface, pos_x: int, pos_y: int, size_x: int, size_y: int):
        length = min(size_x / self.maze.height,
                    size_y / self.maze.width)
        stroke = max(length / 3, 1)
        pygame.draw.rect(screen, (100, 100, 255), (pos_x + stroke + (self.path[-1][0] * length), pos_y +
                stroke + (self.path[-1][1] * length), length - (2 * stroke), length - (2 * stroke)))
        pygame.draw.rect(screen, (50, 50, 255), (pos_x + stroke + (self.path[-1][0] * length), pos_y +
                stroke + (self.path[-1][1] * length), length - (2 * stroke), length - (2 * stroke)), int(stroke) // 5)

    def draw(self, screen: pygame.Surface, pos_x: int, pos_y: int, size_x: int, size_y: int):
        screen_x, screen_y = screen.get_size()
        length = min(size_x / self.maze.height,
                     size_y / self.maze.width)
        stroke = max(length / 3, 1)
        last_x = 0
        last_y = 0
        for (cell_x, cell_y) in self.path:
            if (last_x < cell_x):
                pygame.draw.rect(screen, (50, 50, 255), (pos_x + stroke + (last_x * length), pos_y +
                                 stroke + (last_y * length), 2 * length - (2 * stroke), length - (2 * stroke)))
            elif (last_x > cell_x):
                pygame.draw.rect(screen, (50, 50, 255), (pos_x + stroke + (cell_x * length), pos_y +
                                 stroke + (cell_y * length), 2 * length - (2 * stroke), length - (2 * stroke)))
            elif (last_y < cell_y):
                pygame.draw.rect(screen, (50, 50, 255), (pos_x + stroke + (last_x * length), pos_y +
                                 stroke + (last_y * length), length - (2 * stroke), 2 * length - (2 * stroke)))
            elif (last_y > cell_y):
                pygame.draw.rect(screen, (50, 50, 255), (pos_x + stroke + (cell_x * length), pos_y +
                                 stroke + (cell_y * length), length - (2 * stroke), 2 * length - (2 * stroke)))
            last_x = cell_x
            last_y = cell_y
