from Cell import Cell
import pygame

class Maze:
    grid: list[list[Cell]] = [[]]
    width: int
    height: int

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        for i in range(height):
            self.grid.append([])
            for j in range(width):
                self.grid[i].append(Cell(0))

    def __init__(self, width: int, height: int, default_wall: int):
        self.width = width
        self.height = height
        for i in range(height):
            self.grid.append([])
            for j in range(width):
                self.grid[i].append(Cell(default_wall))

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, (100, 100, 100), (10, 10, 10 * self.width, 10 * self.height))
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, (255, 0, 0), (10 + (i * 10), 10 + (j * 10), 10, 10))
        return 0
