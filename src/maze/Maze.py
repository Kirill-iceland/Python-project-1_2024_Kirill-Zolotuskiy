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
        screen_x, screen_y = screen.get_size()
        length = min(screen_y / (self.height + 2), screen_x / (self.width + 2))
        pygame.draw.rect(screen, (100, 100, 100), (length, length, length * self.width, length * self.height))
        stroke = max(length / 10, 1)
        for i in range(self.height):
            for j in range(self.width):
                if (self.grid[i][j].left_wall):
                    pygame.draw.rect(screen, (255, 0, 0), (length + (i * length), length + (j * length), length, stroke))

                if (self.grid[i][j].right_wall):
                    pygame.draw.rect(screen, (255, 0, 0), (length + (i * length), 2 * length - stroke + (j * length), length, stroke))

                if (self.grid[i][j].top_wall):
                    pygame.draw.rect(screen, (255, 0, 0), (length + (i * length), length + (j * length), stroke, length))

                if (self.grid[i][j].bottom_wall):
                    pygame.draw.rect(screen, (255, 0, 0), (2 * length - stroke + (i * length), length + (j * length), stroke, length))
        return 0
