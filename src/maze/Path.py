import pygame
from Maze import Maze


class Path:
    maze: Maze
    path: list[tuple[int, int]] = []

    def __init__(self, maze):
        self.path = []
        self.maze = maze

    def append(self, cell_x: int, cell_y: int):
        self.path.append((cell_x, cell_y))

    def draw(self, screen: pygame.Surface, pos_x: int, pos_y: int, size_x: int, size_y: int):
        screen_x, screen_y = screen.get_size()
        length = min(size_x / self.maze.height,
                     size_y / self.maze.width)
        stroke = max(length / 5, 1)
        for (cell_x, cell_y) in self.path:
            pygame.draw.rect(screen, (50, 50, 255), (pos_x + stroke + (cell_x * length), pos_y +
                             stroke + (cell_y * length), length - (2 * stroke), length - (2 * stroke)))
            pygame.draw.rect(screen, (150, 150, 150), (pos_x + stroke + (cell_x * length), pos_y +
                             stroke + (cell_y * length), length - (2 * stroke), length - (2 * stroke)), int(stroke) // 2)
