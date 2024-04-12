import pygame

from src.maze.Cell import Cell

class Maze:
    def __init__(self, width: int, height: int):
        self.grid = [[]]
        self.width = width
        self.height = height
        for i in range(height):
            self.grid.append([])
            for j in range(width):
                self.grid[i].append(Cell(0))

    def __init__(self, width: int, height: int, default_wall: int):
        self.grid = [[]]
        self.width = width
        self.height = height
        for i in range(height):
            self.grid.append([])
            for j in range(width):
                self.grid[i].append(Cell(default_wall))

    def draw(self, screen: pygame.Surface, pos_x: int, pos_y: int, size_x: int, size_y: int):
        pos_x = float(pos_x)
        pos_y = float(pos_y)
        screen_x, screen_y = screen.get_size()
        length = min(size_x / self.height,
                     size_y / self.width)
        pygame.draw.rect(screen, (100, 100, 100), (pos_x,
                         pos_y, length * self.height, length * self.width))
        pygame.draw.rect(screen, (255, 255, 100),
                         (pos_x, pos_y, length, length))
        pygame.draw.rect(screen, (100, 255, 100), ((length * (self.height - 1)) +
                         pos_x, (length * (self.width - 1)) + pos_y, length, length))
        stroke = max(length / 10, 1)
        for i in range(self.height):
            for j in range(self.width):
                if (self.grid[i][j].left_wall):
                    pygame.draw.rect(
                        screen, (255, 0, 0), (pos_x + (i * length), pos_y + (j * length), length, stroke + 1))

                if (self.grid[i][j].right_wall):
                    pygame.draw.rect(screen, (255, 0, 0), (pos_x + (i * length),
                                     pos_y + length - stroke + (j * length), length, stroke + 1))

                if (self.grid[i][j].top_wall):
                    pygame.draw.rect(
                        screen, (255, 0, 0), (pos_x + (i * length), pos_y + (j * length), stroke + 1, length))

                if (self.grid[i][j].bottom_wall):
                    pygame.draw.rect(screen, (255, 0, 0), (pos_x +  length - stroke +
                                     (i * length), pos_y + (j * length), stroke + 1, length))

    def get_edges(self) -> list[list[list[tuple[int, int]]]]:
        edges = [[[]]]
        for i in range(self.height):
            edges.append([[]])
            for j in range(self.width):
                edges[i].append([])
                if (j + 1 < self.width and not self.grid[i][j].right_wall):
                    edges[i][j].append((i, j + 1, 0))
                if (j > 0 and not self.grid[i][j].left_wall):
                    edges[i][j].append((i, j - 1, 1))
                if (i + 1 < self.height and not self.grid[i][j].bottom_wall):
                    edges[i][j].append((i + 1, j, 2))
                if (i > 0 and not self.grid[i][j].top_wall):
                    edges[i][j].append((i - 1, j, 3))
        return edges
