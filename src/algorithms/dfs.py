import sys
import random

from src.maze.maze import Maze

class DFS:
    def DFS(top_x: int, top_y: int, edges: list[list[list[tuple[int, int, int]]]],
            maze: Maze, visited: list[list[bool]]):
        visited[top_x][top_y] = True
        random.shuffle(edges[top_x][top_y])

        for (cell_x, cell_y, wall_type) in edges[top_x][top_y]:
            if visited[cell_x][cell_y]:
                continue
            if (wall_type == 0):
                maze.grid[top_x][top_y].right_wall = False
                maze.grid[cell_x][cell_y].left_wall = False
            elif (wall_type == 1):
                maze.grid[top_x][top_y].left_wall = False
                maze.grid[cell_x][cell_y].right_wall = False
            elif (wall_type == 2):
                maze.grid[top_x][top_y].bottom_wall = False
                maze.grid[cell_x][cell_y].top_wall = False
            elif (wall_type == 3):
                maze.grid[top_x][top_y].top_wall = False
                maze.grid[cell_x][cell_y].bottom_wall = False
            DFS.DFS(cell_x, cell_y, edges, maze, visited)

    def generate(width: int, height: int) -> Maze:
        sys.setrecursionlimit(width * height * 10)
        maze = Maze(width, height, 0b1111)
        edges = [[[]]]
        visited = [[]]

        for i in range(height):
            edges.append([[]])
            visited.append([])
            
            for j in range(width):
                visited[i].append(False)
                edges[i].append([])
                if (j + 1 < width):
                    edges[i][j].append((i, j + 1, 0))
                if (j > 0):
                    edges[i][j].append((i, j - 1, 1))
                if (i + 1 < height):
                    edges[i][j].append((i + 1, j, 2))
                if (i > 0):
                    edges[i][j].append((i - 1, j, 3))

        DFS.DFS(0, 0, edges, maze, visited)
        return maze
