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
        length = min(screen_y / (self.height + 2),
                     screen_x / (self.width + 2))
        pygame.draw.rect(screen, (100, 100, 100), (length,
                         length, length * self.height, length * self.width))
        pygame.draw.rect(screen, (255, 255, 100),
                         (length, length, length, length))
        pygame.draw.rect(screen, (100, 255, 100), ((
            length * self.height), (length * self.width), length, length))
        stroke = max(length / 10, 1)
        for i in range(self.height):
            for j in range(self.width):
                if (self.grid[i][j].left_wall):
                    pygame.draw.rect(
                        screen, (255, 0, 0), (length + (i * length), length + (j * length), length, stroke))

                if (self.grid[i][j].right_wall):
                    pygame.draw.rect(screen, (255, 0, 0), (length + (i * length),
                                     2 * length - stroke + (j * length), length, stroke))

                if (self.grid[i][j].top_wall):
                    pygame.draw.rect(
                        screen, (255, 0, 0), (length + (i * length), length + (j * length), stroke, length))

                if (self.grid[i][j].bottom_wall):
                    pygame.draw.rect(screen, (255, 0, 0), (2 * length - stroke +
                                     (i * length), length + (j * length), stroke, length))

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
