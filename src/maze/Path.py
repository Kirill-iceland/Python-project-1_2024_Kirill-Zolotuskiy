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

    def draw(self, screen: pygame.Surface):
        screen_x, screen_y = screen.get_size()
        length = min(screen_y / (self.maze.height + 2),
                     screen_x / (self.maze.width + 2))
        stroke = max(length / 5, 1)
        for (cell_x, cell_y) in self.path:
            pygame.draw.rect(screen, (50, 50, 255), (length + stroke + (cell_x * length), length +
                             stroke + (cell_y * length), length - (2 * stroke), length - (2 * stroke)))
            pygame.draw.rect(screen, (150, 150, 150), (length + stroke + (cell_x * length), length +
                             stroke + (cell_y * length), length - (2 * stroke), length - (2 * stroke)), int(stroke) // 2)
